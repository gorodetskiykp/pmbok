from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.ProjectListView.as_view(), name='projects-list'),
    path('<int:pk>/', views.ProjectDetailView.as_view(), name='project-details'),
]
