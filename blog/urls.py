from . import views
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', views.home, name="home"),
    path('post/<post_slug>/', views.posts, name='post_detail'),
    path('authors/', views.authors, name='authors_detail'),
]
