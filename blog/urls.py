#Aqui esta sendo importado a funçao url e todas as views do app blog.
from django import urls
from django.conf.urls import url
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]