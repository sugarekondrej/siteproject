

from django.urls import path,include
from . import views
urlpatterns = [
   path("",views.index,name="listings"),
   path("search",views.search,name="search"),
    path("<int_listing_id>",views.listing,name="listing"),
  


]
