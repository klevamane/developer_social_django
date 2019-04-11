from django.shortcuts import render
from rest_framework import generics
from .models import Education
from .serializers import EducationSerializer
from developer.permission_helpers import IsOwnerOrReadOnly
# Create your views here.


class ListCreate (generics.ListCreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class RetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = (IsOwnerOrReadOnly,)