from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from .models import Card
from .serializers import CardSerializer,CommentSerializer

class CardList(generics.ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
