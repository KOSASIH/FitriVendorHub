from django.shortcuts import render
from.models import Document

def document_list(request):
    documents = Document.objects.all()
    return render(request, 'document_list.html', {'documents': documents})

def document_detail(request, pk):
    document = Document.objects.get(pk=pk)
    return render(request, 'document_detail.html', {'document': document})
