

from django.urls import path,include
from . import views
urlpatterns = [
   path("listings",views.index,name="listings"),
   path("search",views.search,name="search"),
    path("<int:listing_id>",views.listing,name="listing"),
  


]
