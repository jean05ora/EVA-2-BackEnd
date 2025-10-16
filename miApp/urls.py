from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('fragancias/', views.fragancias, name='categoria-fragancias'),
    path('poleras/', views.poleras, name='categoria-poleras'),
    path('categorias/', views.categorias, name='categorias')
]
