# Generated by Django 5.0.7 on 2024-07-16 15:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("idea", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="content",
            field=models.TextField(verbose_name="아이디어 설명"),
        ),
        migrations.AlterField(
            model_name="post",
            name="devtool",
            field=models.CharField(
                choices=[
                    ("django", "Django"),
                    ("react", "React"),
                    ("spring", "Spring"),
                    ("nodejs", "Node.js"),
                    ("java", "Java"),
                    ("cpp", "C++"),
                ],
                max_length=20,
                verbose_name="예상 개발툴",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="interest",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(10),
                ],
                verbose_name="아이디어 관심도",
            ),
        ),
    ]
