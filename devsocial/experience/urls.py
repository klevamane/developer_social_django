from django.urls import path
from .views import ExperienceListCreate, ExperienceDetailsAPIView

urlpatterns = [
    path('', ExperienceListCreate.as_view(), name='experience_create_list'),
    path('<int:pk>/', ExperienceDetailsAPIView.as_view(), name='experience_details')
]