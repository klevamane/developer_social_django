from django.db import models
from developer.models import Developer


# Create your models here.
class Experience(models.Model):
    organization = models.CharField(max_length=200)
    location = models.CharField(max_length=100, blank=True)
    _from = models.DateField()
    to = models.DateField(blank=True, null=True)
    designation = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=200, blank=True)
    # the related name here enables the developer model to implement Developer.experiences
    developer = models.ForeignKey(Developer, related_name='experiences', on_delete=models.CASCADE)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
