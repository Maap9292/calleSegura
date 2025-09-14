from django.urls import path
from . import views_frontend
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views_frontend.reporte_list, name='reporte_list'),
    path('nuevo/', views_frontend.reporte_create, name='reporte_create'),
    path('<int:pk>/', views_frontend.reporte_detail, name='reporte_detail'),
    path('<int:pk>/cambiar_estado/', views_frontend.cambiar_estado, name='reporte_cambiar_estado'),
    path('login/', auth_views.LoginView.as_view(template_name='reportes/login.html'), name='login'),
    path(
    'logout/',
    auth_views.LogoutView.as_view(next_page='/reportes/'),
    name='logout'
    ),
]




