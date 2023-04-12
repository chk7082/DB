from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
#
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.http import require_POST, require_safe, require_http_methods
from .forms import CustomUserCreationForm, CustomUserChangeForm

from django.contrib.auth import get_user_model


# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('articles:index')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index') 
    else:
        form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)

@require_http_methods(['POST'])
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('articles:index')

def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index') 
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {'form': form}
    return render(request, 'accounts/update.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('articles:index') 
    else:
        form = PasswordChangeForm(request.user)
    context = {'form': form}
    return render(request, 'accounts/change_password.html', context)


def profile(request, username):
    person = get_user_model().objects.get(username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)


@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        person = get_user_model().objects.get(pk=user_pk)
        # 자기자신이랑 다른 사람이어야 팔로우가 의미 있다
        # 지금 팔로우 상태라면 언팔
        # 지금 언팔 상태라면 팔로우
        if person != request.user:
            # 저 사람의 팔로워 목록에 request한 유저가 존재하면 언팔
            if person.followers.filter(pk=request.user.pk).exists():
                person.followers.remove(request.user)
            # 존재하지 않으면 follow
            else:
                person.followers.add(request.user)
        # 그 사람의 프로필 페이지에서 동작하는거니까 거기로 redirect!!
        return redirect('accounts:profile', person.username)
    return redirect('accounts:login')