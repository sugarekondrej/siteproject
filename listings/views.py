from ast import keyword
from django.shortcuts import render
from . import models
from listings import urls
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from listings.choices import state_choices,bedroom_choices,price_choices

# Create your views here.
def index(request):
    listings = models.Listings.objects.all()

    paginator = Paginator(listings,3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
            'listings': paged_listings,
           

    }
    return render(request,'listings/listings.html',context)

def listing(request,listing_id):
    listing = models.Listings.objects.get(pk=listing_id)

    context = {
        "listing": listing
    }

    return render(request,'listings/listing.html',context)

def search(request):
    query_list = models.Listings.objects.order_by('-list_date')

    #keyword
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            query_list = query_list.filter(description__icontains=keywords)
    #city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            query_list = query_list.filter(city__iexact=city)
    #state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            query_list = query_list.filter(state__iexact=state)
    #bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            query_list = query_list.filter(bedrooms__iexact=bedrooms)
    #price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            query_list = query_list.filter(price__lte=price)

    
    context = {
        "bedroom_choices": bedroom_choices,
        "price_choices":price_choices,
        "state_choices": state_choices,
        "listings": query_list
        }


    

    return render(request,'listings/search.html',context)