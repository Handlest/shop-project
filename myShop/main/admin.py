from django.contrib import admin
from .models import Product, Category, Type


admin.site.register(Type)
admin.site.register(Category)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'category', 'price', 'is_available']
    list_filter = ['name', 'type', 'category', 'price', 'is_available']
    list_editable = ['price', 'is_available']


admin.site.register(Product, ProductAdmin)

#     name = models.CharField(verbose_name="Категория", max_length=64, unique=True)
#     extra = models.CharField(verbose_name="Дополнительно")
#
#
# class Product(models.Model):
#     name = models.CharField(verbose_name="Название", max_length=64, default='')
#     type = models.CharField(verbose_name="Тип(Цветок/сопутствующий товар..)", max_length=64, default='')
#     category = models.CharField(verbose_name="Категория", max_length=64, default='')
#     price = models.IntegerField(verbose_name="Цена")
#     is_available = models.BooleanField(verbose_name="Доступность к покупке", default=False)
#     picture = models.ImageField(verbose_name="Изображение", default="myShop/main/static/main/img/begonia_pic.jpg")
#     description = models.TextField(verbose_name="Описание", default='')
