from django.db import models
from django.core.validators import MinValueValidator
from datetime import datetime


# Товар для нашей витрины
class Post(models.Model):
    title = models.CharField(
        max_length=50,
        unique=True,  # названия товаров не должны повторяться
    )
    text = models.TextField()
    time_in = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(
        validators=[MinValueValidator(0)],
    )
    # поле категории будет ссылаться на модель категории
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='Category',  # все продукты в категории будут доступны через поле products
    )


    def __str__(self):
        return f'{self.title}: {self.text}'



# Категория, к которой будет привязываться товар
class Category(models.Model):
    # названия категорий тоже не должны повторяться
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
