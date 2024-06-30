from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def linkbuilding(request):
    return render(request, 'lb.html')