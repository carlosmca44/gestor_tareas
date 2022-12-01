from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('eliminar/<int:tarea_id>/',views.eliminar, name='eliminar'),
    path('editar/<int:tarea_id>/',views.editar, name='editar'),
    path('personal', views.personal, name='personal'),
    path('trabajos', views.trabajos, name='trabajos'),
    path('lista', views.lista, name='lista'),
    path('birthday', views.birthday, name='birthday')
]