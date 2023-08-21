from django.db import models


# Create your models here.

class Type(models.Model):
    name = models.CharField(verbose_name="Тип товара", max_length=64, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'


class Category(models.Model):
    name = models.CharField(verbose_name="Категория", max_length=64, unique=True)
    extra = models.CharField(verbose_name="Дополнительно", max_length=128, null=True, blank=True, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(verbose_name="Название", max_length=64, default='')
    type = models.ForeignKey(Type, related_name='types', on_delete=models.PROTECT, verbose_name="Тип")
    category = models.ForeignKey(Category, related_name='categories', on_delete=models.PROTECT, verbose_name="Категория")
    price = models.DecimalField(verbose_name="Цена", decimal_places=2, max_digits=12)
    is_available = models.BooleanField(verbose_name="Доступность к покупке", default=False)
    picture = models.ImageField(verbose_name="Изображение",
                                default="myShop/main/static/main/img/default.jpg")  # Fix default image
    description = models.TextField(verbose_name="Описание", default='', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
