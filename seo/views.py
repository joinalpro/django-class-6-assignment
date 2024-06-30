from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def seo(request):
    return render(request, 'seo.html')