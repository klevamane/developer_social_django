from django.db import models
import re
from django.core.exceptions import ValidationError
from rest_framework import status
# Create your models here.


def validate_mobile_number(value):
    """Validate the mobile number to ascertain it is of nigerian format"""
    result = re.findall('[0][7,8,9][0-9]{9}', value)
    if not result:
        raise ValidationError('The mobile number must be of Nigerian mobile format', status.HTTP_400_BAD_REQUEST)


class Developer(models.Model):
    """This is the developer model class"""
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    description = models.TextField()
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True, error_messages={'unique': 'A user with the same email already exist'})
    twitter = models.URLField(max_length=200, blank=True,)
    instagram = models.URLField(max_length=200, blank=True)
    linkedin = models.URLField(max_length=200, blank=True)
    facebook = models.URLField(max_length=200, blank=True)
    github = models.URLField(max_length=200, blank=True)
    mobile = models.CharField(max_length=11, unique=True,
        error_messages={'unique': 'A user already registered with this mobile number'}, validators=[validate_mobile_number])
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return "{} {}".format(self.firstname, self.lastname)

