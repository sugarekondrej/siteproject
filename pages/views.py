from multiprocessing import context
from urllib import request
from django.shortcuts import render
from listings import models
from listings.choices import state_choices,bedroom_choices,price_choices
# Create your views here.
def index(request):
    listings = models.Listings.objects.all()
    context = {
        "listings":listings,
        "bedroom_choices": bedroom_choices,
        "price_choices":price_choices,
        "state_choices": state_choices

    }

    return render(request,'pages/index.html',context)


def about(request):
    return render(request,'pages/about.html')