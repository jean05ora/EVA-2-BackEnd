from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('detalles-fragancia/<int:id>', views.detalles_fragancia, name='detalles-fragancia'),
    path('detalles-polera/<int:id>', views.detalles_polera, name='detalles-polera'),
    path('fragancias/', views.fragancias, name='categoria-fragancias'),
    path('poleras/', views.poleras, name='categoria-poleras'),
    path('categorias/', views.categorias, name='categorias')
]
