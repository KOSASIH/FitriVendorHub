from django.shortcuts import render
from.models import VendorPerformance

def vendor_performance_list(request):
    vendor_performances = VendorPerformance.objects.all()
    return render(request, 'endor_performance_list.html', {'vendor_performances': vendor_performances})

def vendor_performance_detail(request, pk):
    vendor_performance = VendorPerformance.objects.get(pk=pk)
    return render(request, 'endor_performance_detail.html', {'vendor_performance': vendor_performance})
