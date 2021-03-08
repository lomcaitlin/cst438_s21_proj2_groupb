from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path(('login/', auth_views.loginView.as_view(), name='login'),
    path('logout/'), auth_views.loginView.as_view(), name='logout'),
    
]