from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import ExperienceSerializer

from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework import status
from .models import Experience as ExperienceModel
from developer.models import Developer
# Create your views here.


def check_if_developerExist(developer_id):
    try:
        Developer.objects.get (pk=developer_id)
    except Developer.DoesNotExist:
        raise ObjectDoesNotExist('message')


class ExperienceListCreate(APIView):

    """Implement the post http"""
    def get(self, request, format=None):
        experiences = ExperienceModel.objects.all()
        serializer = ExperienceSerializer(experiences, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        request_body = {}
        for key, value in request.data.items():
            request_body[key] = value
        if request_body.get('developer') is None:
            request_body['developer'] = request.user
        check_if_developerExist(request.data.get('developer'))
        serializer = ExperienceSerializer(data=request_body)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data,status.HTTP_200_OK)


class ExperienceDetailsAPIView(APIView):
    def get_object(self, pk):
        try:
            return ExperienceModel.objects.get(pk=pk)
        except ExperienceModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        experience = self.get_object(pk)
        serializer = ExperienceSerializer(data=experience, many=True)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        experience = self.get_object(pk)
        serializer = ExperienceSerializer(experience, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        experience = ExperienceModel.objects.get(pk)
        serializer = ExperienceSerializer(experience)
        serializer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)