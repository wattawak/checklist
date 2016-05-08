from .models import Task
from django.shortcuts import render


def Index(request):
	items = Task.objects.order_by('due_date')
	return render(request, 'checklist/index.html', {'items': items})
