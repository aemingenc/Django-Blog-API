from django.urls import path
from .views import CardDetail,CardList,CardPost

urlpatterns = [
 

    path("card-detail/<int:pk>/", CardDetail.as_view()),
    path("list/",CardList.as_view(),name ="card_list"),
    path("post/",CardPost.as_view(),name ="card_list"),
    
 ]