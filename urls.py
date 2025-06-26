from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('job/<int:pk>/', views.job_detail, name='job_detail'),
    path('privacy/', views.privacy, name='privacy'),
    path('search/', views.job_search, name='job_search'),
] 