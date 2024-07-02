from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def linkbuilding(request):
    return render(request, 'linkbuilding/lb.html', {'method': 4, 'member': 'ahpro'})

def link_building_list(request):
    haro= 'HARO the most powerful link buildinge technique'
    shotgun='Shotgun method work in average'
    skyscraper = 'SkyScrapper the brian dean method'
    guestpost = 'GuestPost now so difficult to gain real link'
    
    lb_details = {'haro':haro, 'shotgun': shotgun, 'skyscraper': skyscraper, 'guestpost': guestpost}
    
    return render(request, 'linkbuilding/lb_list.html', lb_details)