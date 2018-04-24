from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Project


class ProjectListView(ListView):
    model = Project
    context_object_name = 'projects_list'


class ProjectDetailView(DetailView):
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #self.request.session['project_name'] = "short_name" 
        self.request.session['project_title'] = self.object.short_name 
        return context
