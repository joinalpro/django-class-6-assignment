from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def seo(request):
    seo_checklist = {'seo': ['Onpage','keyword', 'internal linking', 'external linking', 'content-optimization']}
    return render(request, 'seo/seo.html',seo_checklist)

def seo_checklist(request):
    return render(request,'seo/seo-checklist.html')