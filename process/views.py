from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Process


class ProcessListView(ListView):
    model = Process
