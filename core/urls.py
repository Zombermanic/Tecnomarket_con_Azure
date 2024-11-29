from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('agregar-producto/', views.agregar_producto, name='agregar_producto'),
    path('listar-productos/', views.listar_productos, name='listar_productos'),
    path('modificar-producto/<id>/', views.modificar_producto, name='modificar_producto'),
    path('eliminar-producto/<id>/', views.eliminar_producto, name='eliminar_producto'),
    path('registro/', views.registro, name='registro'),

]