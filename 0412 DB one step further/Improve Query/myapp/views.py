from django.shortcuts import render
from .models import PetSitter, Pet

from django.db import connection
from django.db import reset_queries

# Create your views here.


def get_sql_queries(origin_func):
    def wrapper(*args, **kwargs):
        # 어떤 함수 전에 실행할거
        reset_queries()

        # original 함수
        origin_func(*args, **kwargs) # 저 뒤에 어떤 이자가 오던지 다 가능하겠다

        # original 함수 뒤에 처리할거
        query_info = connection.queries
        for query in query_info:
            print(query['sql'])
    
    return wrapper


# 요청, 응답이 아니라 그냥 함수 만들고 싶다
@get_sql_queries
def get_pet_data():
    # reset_queries()

    # pets = Pet.objects.all()
    pets = Pet.objects.all().select_related('pet_sitter')
    for pet in pets:
        print(f'{pet.name} | 집사 : {pet.pet_sitter.first_name}')

    query_info = connection.queries

    # # query가 dict형태
    # for query in query_info:
    #     print(query['sql']) # 내가 쓴 ORM이 어떤 식으로 SQL 나가는지 출력해주는 코드