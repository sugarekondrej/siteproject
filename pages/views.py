from multiprocessing import context
from urllib import request
from django.shortcuts import render
from listings import models
# Create your views here.
def index(request):
    listings = models.Listings.objects.all()
    context = {
        "listings":listings
    }

    return render(request,'pages/index.html',context)


def about(request):
    return render(request,'pages/about.html')