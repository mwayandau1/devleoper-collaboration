from django.urls import path
from .import views


urlpatterns =[
    path('', views.getRoutes),
    path('projects/', views.getProjects),
    path('projects/<str:pk>/', views.get_single_project),
    path('remove-tag/', views.removeTag),
]