from django.shortcuts import render
from.models import Translation

def translation_list(request):
    translations = Translation.objects.all()
    return render(request, 'translation_list.html', {'translations': translations})

def translation_detail(request, pk):
    translation = Translation.objects.get(pk=pk)
    return render(request, 'translation_detail.html', {'translation': translation})
