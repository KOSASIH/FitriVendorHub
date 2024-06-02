from django.shortcuts import render
from.models import Notification

def notification_list(request):
    notifications = Notification.objects.all()
    return render(request, 'notification_list.html', {'notifications': notifications})

def notification_detail(request, pk):
    notification = Notification.objects.get(pk=pk)
    return render(request, 'notification_detail.html', {'notification': notification})
