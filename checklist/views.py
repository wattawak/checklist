from .models import Task
from django.shortcuts import render


def Index(request):
	items = Task.objects.all()
	return render(request, 'checklist/index.html', {'items': items})
