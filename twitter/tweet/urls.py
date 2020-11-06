from django.urls import path
from tweet import views

urlpatterns = [
    path('', views.tweet, name='tweet'),
    path('home', views.home, name='home'),
    path('posttweet', views.posttweet, name='posttweet'),
    path('process_form', views.process_form, name='process_form'),
    path('detail', views.detail, name='detail'),
]
