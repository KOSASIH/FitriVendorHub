from django.shortcuts import render
from.models import Integration

def integration_list(request):
    integrations = Integration.objects.all()
    return render(request, 'integration_list.html', {'integrations': integrations})

def integration_detail(request, pk):
    integration = Integration.objects.get(pk=pk)
    return render(request, 'integration_detail.html', {'integration': integration})
