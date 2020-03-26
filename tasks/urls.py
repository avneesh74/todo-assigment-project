from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="list"),
    path('update_tasks/<str:pk>/', views.updateTasks, name="update_task"),
    path('delete/<str:pk>/', views.deleteTask, name="delete"),
]
