from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('detalles-fragancia/<int:id>', views.detalles_fragancia, name='detalles-fragancia'),
    path('detalles-polera/<int:id>', views.detalles_polera, name='detalles-polera'),
<<<<<<< HEAD
    path('fragancias/', views.fragancias, name='categoria-fragancias'),
    path('poleras/', views.poleras, name='categoria-poleras'),
    path('categorias/', views.categorias, name='categorias')
=======
    path('categorias/', views.categorias, name = 'categorias'),
    path('categoria_fragancia/', views.categoria_fragancia, name='categoria_fragancia'),
    path('categoria_polera/', views.categoria_polera, name='categoria_polera')
>>>>>>> master
]
