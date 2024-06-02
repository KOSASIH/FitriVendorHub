from django.shortcuts import render
from.models import File

def file_list(request):
    files = File.objects.all()
    return render(request, 'file_list.html', {'files': files})

def file_detail(request, pk):
    file = File.objects.get(pk=pk)
    return render(request, 'file_detail.html', {'file': file})
