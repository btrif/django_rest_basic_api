from django.shortcuts import render
from rest_framework import viewsets
from .models import Lanaguage
from .serializers import LanguageSerializer

# Create your views here.
class LanguageView(viewsets.ModelViewSet):
    queryset = Lanaguage.objects.all()
    serializer_class = LanguageSerializer

