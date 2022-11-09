from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view

urlpatterns = [
    path("", views.index, name = 'home'),
    # path('', views.home, name='home'),
     path('register/', views.register, name='register'),
      path('profile/', views.profile, name='profile'),
    path('login/', auth_view.LoginView.as_view(template_name='home/login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='home/logout.html'), name="logout"),
    path('category/<int:cid>/', views.showCategoryPage)
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)