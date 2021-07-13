from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='blog-register'),
    path('login/', views.login_page, name='blog-login'),
    path('logout/', views.logout_page, name='blog-logout')
]