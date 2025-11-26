from django.urls import path
from . import views


urlpatterns = [
    path('',views.homepage),
    path('tour',views.tours),
    path('book',views.bookmytrip),
    path('tourdetails',views.tourdetails),
    path('aboutus',views.about_us),
    path('rating',views.rating),
        
]

