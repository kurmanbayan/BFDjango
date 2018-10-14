from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blogs, name="blog"),
    path('blog/add/', views.addBlog, name="addblog"),
    path('comment/<int:id>/', views.comments, name="comments"),
    path('comment/<int:id>/add/', views.addComment, name="addcomment"),
]
