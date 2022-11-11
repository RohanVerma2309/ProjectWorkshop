from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('upload/', views.upload, name='upload'),
<<<<<<< HEAD
    path('editor/', views.edit, name='editor'),
=======
    # path('home/', views.home, name='home'),
>>>>>>> 274fb4f9501dcac0b5f059c37f2f2db4c2726d90
    path('profile/', views.profile, name='profile'),
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
]
