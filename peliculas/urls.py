from . import views
from django.urls import path

urlpatterns =[
    path('', views.inicio, name='inicio'),
    path('ayuda', views.ayuda, name='ayuda'),
    path('peliculas', views.peliculas, name='peliculas'),
    path('peliculas/agregar', views.agregar, name='agregar'),
    path('peliculas/editar/<int:id>', views.editar, name='editar'),
    path('peliculas/eliminar/<int:id>', views.eliminar, name='eliminar')
]