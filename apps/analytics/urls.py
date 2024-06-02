from django.urls import path
from. import views

urlpatterns = [
    path('vendor_performances/', views.vendor_performance_list, name='vendor_performance_list'),
    path('vendor_performances/<pk>/', views.vendor_performance_detail, name='vendor_performance_detail'),
]
