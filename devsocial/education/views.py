from django.shortcuts import render
from rest_framework import generics
from .models import Education
from .serializers import EducationSerializer
# Create your views here.


class ListCreate (generics.ListCreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class RetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer