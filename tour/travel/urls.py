from django.urls import path
from . import views

app_name = 'travel'

urlpatterns = [

    path('index/', views.index , name='index'),
    path('', views.FirstPage, name='FirstPage'),
    path('secondpage/', views.secondpage, name='secondpage'),
    path('therdpage/', views.therdpage, name='therdpage'),
    path('ForthPage/', views.ForthPage, name='ForthPage'),
]