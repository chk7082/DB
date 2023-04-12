from django.db import models

from imagekit.processors import Thumbnail, ResizeToFill, SmartResize
from imagekit.models import ProcessedImageField, ImageSpecField


class Hashtag(models.Model):
    content = models.CharField(max_length=50, unique=True)


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True)
    thumbnail_img = ImageSpecField(
        source='image',
        processors = [Thumbnail(200, 300)], # 200X300으로 줄이자
        format = 'JPEG', # 어떤 이미지를 넣던지 jpeg로 바꿔서 저장할거야
        options={'quality':80},
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    hashtags = models.ManyToManyField(Hashtag)

    def __str__(self):
        return f'{self.id}번째글 - {self.title}'



class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    parent  = models.ForeignKey('self', 
                                on_delete=models.CASCADE, 
                                null=True, 
                                related_name='replies')
    # 없으면 댓글, 있으면 답글로 하려고



