from process.models import ProcessGroup
from project.models import Project

def menu(request):
    context = {
        'process_groups': ProcessGroup.objects.all(),
        'projects': Project.objects.all(), 
        'project_title': request.session['project_title']
    }
    return context
