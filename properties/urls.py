# ... (previous code)

from django.urls import path
from .views import property_search

urlpatterns = [
    path('search/', property_search, name='property-search'),
    path('results/', property_search,
         name='property-search-results'),  # Add this line
]
