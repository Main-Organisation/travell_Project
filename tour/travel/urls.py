from django.urls import path
from . import views

app_name = 'travel'

urlpatterns = [

    
    path('', views.FirstPage, name='FirstPage'),
    path('index/', views.index , name='index'),
    path('secondpage/', views.secondpage, name='secondpage'),
    path('therdpage/', views.therdpage, name='therdpage'),
    path('Forthpage/', views.ForthPage, name='Forthpage'),
]