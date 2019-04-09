from .views import CreateDeveloper, RetrieveUpdateDestroy
from django.urls import path

urlpatterns = [
    path('', CreateDeveloper.as_view(), name='new_developer'),
    path('<int:pk>/', RetrieveUpdateDestroy.as_view(), name='update_delete_view')
]
