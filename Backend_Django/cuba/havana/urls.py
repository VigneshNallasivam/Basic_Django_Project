from django.urls import path
from . import views
urlpatterns = [
    path('havana/', views.havanas, name='havanas'),
]