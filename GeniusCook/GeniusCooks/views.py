from django.shortcuts import render
from rest_framework import viewsets
from .models import Recipe
from rest_framework.generics import DestroyAPIView,UpdateAPIView
from .serializers import RecipeSerializer

class RecipeView(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
class RecipeDelView(DestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    lookup_field = 'profile'
class RecipeUpdateView(UpdateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    lookup_field = 'profile'
# Create your views here.


