from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import DeveloperSerializer
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404

from .models import Developer
# Create your views here.


class CreateDeveloper(CreateAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer


class RetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    """This class implements the GET one, PUT and DELETE http request methods"""
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer