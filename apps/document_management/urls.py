from django.urls import path
from. import views

urlpatterns = [
    path('notifications/', views.notification_list, name='notification_list'),
    path('notifications/<pk>/', views.notification_detail, name='notification_detail'),
]
