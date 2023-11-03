from django.urls import path
from app import views

urlpatterns = [
    path('', view=views.index, name='index'),
    path('post_blog', view=views.post_blog, name='post_blog'),
    path('post_comment/<int:id>', view=views.post_comment, name='post_comment'),
]
