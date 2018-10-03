from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blogs),
    path('comment/<int:id>/', views.comments, name="comments"),
    path('blog/add/', views.addBlog, name="addblog"),
]
