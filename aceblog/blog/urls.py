from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('',PostListView.as_view(),name="blog-home"),
    path('post/<int:pk>/',PostDetailView.as_view(),name="post-detail"),
    path('post/<int:pk>/edit/',PostUpdateView.as_view(),name="post-edit"),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name="post-delete"),
    path('post/new/',PostCreateView.as_view(),name="post-create"),
    path('about/',AboutPageView.as_view(),name="blog-about"),
    path('post/<int:pk>/entry/', views.add_comment_to_post, name='add_comment_to_post'),
]

