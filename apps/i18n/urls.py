from django.urls import path
from. import views

urlpatterns = [
    path('translations/', views.translation_list, name='translation_list'),
    path('translations/<pk>/', views.translation_detail, name='translation_detail'),
]
