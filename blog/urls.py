from django.urls import path
from .views import CardList

urlpatterns = [
 
     path("",CardList.as_view(),name ="card_list"),
    
 ]