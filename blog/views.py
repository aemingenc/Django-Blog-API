from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from .models import Card
from .serializers import CardSerializer

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, mixins

# class CardList(generics.ListAPIView):
#     queryset = Card.objects.all()
#     serializer_class = CardSerializer

class CardList(mixins.ListModelMixin,mixins.CreateModelMixin ,GenericAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CardPost(mixins.CreateModelMixin ,GenericAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
# class CardList(APIView):

#     def get(self, request):
#         cards = Card.objects.all()
#         serializer = CardSerializer(cards, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = CardSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CardDetail(APIView):

#tekrar tekrar yazmak yerine 404 ü tek seferde yazdıkve her yerde kullndık
    def get_obj(self, pk):
#obje bulamazsan 404 not found dönemek(get_object_or_404)
#Card modelline git id si pk olanı getir
        return get_object_or_404(Card, pk=pk)

    def get(self, request, pk):
        card = self.get_obj(pk)
        serializer = CardSerializer(card)
        return Response(serializer.data)

    def put(self, request, pk):
        card = self.get_obj(pk)
        serializer = CardSerializer(instance=card, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        card = self.get_obj(pk)
        card.delete()
        data = {
            "message": "Todo succesfully deleted."
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
