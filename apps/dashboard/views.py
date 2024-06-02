from django.shortcuts import render
from.models import DashboardWidget

def dashboard(request):
    widgets = DashboardWidget.objects.all()
    return render(request, 'dashboard.html', {'widgets': widgets})
