from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("sign-in/", views.sign_in, name="signIn"),
    path('accounts/login/',
         LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='auth/login.html'), name='logout'),
    path('', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('eliminar/<int:tarea_id>/', views.eliminar, name='eliminar'),
    path('editar/<int:tarea_id>/', views.editar, name='editar'),
    path('personal', views.personal, name='personal'),
    path('trabajos', views.trabajos, name='trabajos'),
    path('lista', views.lista, name='lista'),
    path('birthday', views.birthday, name='birthday'),
    path('binary-search', views.binary_search_view, name='binarySearch'),
    path('hs/', views.heap_sort_view, name='heap')
]
