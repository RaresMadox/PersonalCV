
from django.urls import path
from . import views



urlpatterns = [
    path('',views.home,name="homes"),    
    path('search_pr/',views.search_cont,name="search_pr"),
    path('search_tag/',views.search_tag,name="search_tag"),
    path('search_category/',views.search_category,name="search_category"),
]
