from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .serializers import DeveloperSerializer


from .models import Developer
# Create your views here.


class CreateDeveloper(CreateAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer


class RetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    """This class implements the GET one, PUT and DELETE http request methods"""
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer


