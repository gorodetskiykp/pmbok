from django.urls import path
from . import views 

urlpatterns = [
    path('all/', views.ProcessListView.as_view(), name='process-list'),

]
