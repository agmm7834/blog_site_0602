from django.urls import path
from .views import post_list, post_detail

app_name = 'blog'

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<int:id>/', post_detail, name='post_detail'),

]
