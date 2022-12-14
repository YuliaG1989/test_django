from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import MarvelSerializer
from .models import Marvel

class MarvelList(generics.ListCreateAPIView):
    queryset = Marvel.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = MarvelSerializer # tell django what serializer to use

class MarvelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Marvel.objects.all().order_by('id')
    serializer_class = MarvelSerializer