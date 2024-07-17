from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class DevTool(models.Model):
    name = models.CharField(max_length=50)
    kind = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField('제목', max_length=24)
    image = models.ImageField('이미지', blank=True, upload_to='idea/%Y%m%d')
    content = models.TextField('아이디어 설명')
    interest = models.IntegerField('아이디어 관심도', validators=[MinValueValidator(1), MaxValueValidator(10)])
    devtool = models.CharField(max_length=50, default='django')

    def __str__(self):
        return self.title

class IdeaStar(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('post', 'user')

def get_devtool_choices():
    return [(tool.name, tool.name) for tool in DevTool.objects.all()]





