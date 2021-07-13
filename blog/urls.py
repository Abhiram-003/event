from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('fav/<int:movie_id>', views.fav, name='blog-fav'),
    path('favourite/', views.favourite, name='blog-favourite'),
]