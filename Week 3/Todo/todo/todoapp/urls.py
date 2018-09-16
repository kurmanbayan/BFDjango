from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.todos, name="todos"),
    path('todos/deletelist/', views.deleteAll, name='deletelist'),
    path('todos/completed/', views.completed, name='completed'),
    path('todos/mark/<int:id>/', views.markTodo, name='mark'),
    path('todos/add/', views.add, name="add")
]
