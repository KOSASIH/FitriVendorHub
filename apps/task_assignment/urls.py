from django.urls import path
from. import views

urlpatterns = [
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/<pk>/', views.task_detail, name='task_detail'),
]
