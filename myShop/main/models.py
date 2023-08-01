from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(verbose_name="Название", max_length=64, default='')
    type = models.CharField(verbose_name="Тип(Цветок/сопутствующий товар..)",max_length=64, default='')
    category = models.CharField(verbose_name="Категория", max_length=64, default='')
    price = models.IntegerField(verbose_name="Цена")
    is_available = models.BooleanField(verbose_name="Доступность к покупке", default=False)
    picture = models.ImageField(verbose_name="Изображение", default="myShop/main/static/main/img/begonia_pic.jpg")
    description = models.TextField(verbose_name="Описание", default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
