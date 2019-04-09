from .views import ListCreate, RetrieveUpdateDestroy
from django.urls import path

urlpatterns = [
    path('<int:pk>/', RetrieveUpdateDestroy.as_view(), name='get_education'),
    path('', ListCreate.as_view(), name='new_education')
]
