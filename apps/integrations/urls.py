from django.urls import path
from. import views

urlpatterns = [
    path('integrations/', views.integration_list, name='integration_list'),
    path('integrations/<pk>/', views.integration_detail, name='integration_detail'),
]
