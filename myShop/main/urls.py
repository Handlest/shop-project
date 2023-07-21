from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main'),
    path('about', views.about, name='about'),
    path('sales', views.sales, name='sales'),
    path('catalog', views.catalog, name='catalog'),
    path('faq', views.faq, name='faq'),
]
