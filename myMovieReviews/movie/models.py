from django.db import models

class Review(models.Model):
    title = models.CharField(max_length=32) # 제목
    year_release = models.IntegerField() # 개봉년도
    genre = models.CharField(max_length=10) # 장르
    scope = models.FloatField() # 별점
    running_time = models.FloatField() # 러닝타임
    content = models.TextField() # 리뷰
    director = models.CharField(max_length=10) # 감독
    actor = models.CharField(max_length=10) # 배우
