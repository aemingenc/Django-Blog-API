from django.urls import path
from .views import CardDetail,CardList

urlpatterns = [
 

    path("card-detail/<int:pk>/", CardDetail.as_view()),
    path("list/",CardList.as_view(),name ="card_list"),
    
 ]