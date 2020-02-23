from django.shortcuts import render
from django.http import HttpResponse

from .models import Popular
from .models import Rated
from .models import ShopAll

# Create your views here.

def index(request):
    plr = Popular.objects.all()
    rated = Rated.objects.all()

    return render (request, 'shopapp/index.html', {'plrs' : plr, 'rateds' : rated})


def shop(request):
    shops = ShopAll.objects.all()

    return render(request, 'shopapp/shop.html', {'shop' : shops })

# def popular(request):
#     plrs = Popular.objects.all()
#     return render(request, 'shopapp/index.html' ,{'plrs' : 'plrs' })
