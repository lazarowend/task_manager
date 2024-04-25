from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Task

class ConcludeTask(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        
        task.status = not task.status
        task.save()
                
        return HttpResponse('<td>\n'
                                '<a class="button is-white is-small">Concluído</a>\n'
                            '</td>'
                            )

