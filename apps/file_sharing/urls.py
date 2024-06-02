from django.urls import path
from. import views

urlpatterns = [
    path('files/', views.file_list, name='file_list'),
    path('files/<pk>/', views.file_detail, name='file_detail'),
]
