from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, AbstractBaseUser
import re
from rest_framework import status
# Create your models here.


def validate_mobile_number(value):
    """Validate the mobile number to ascertain it is of nigerian format"""
    result = re.findall('[0][7,8,9][0-9]{9}', value)
    if not result:
        raise ValueError('The mobile number must be of Nigerian mobile format', status.HTTP_400_BAD_REQUEST)


class DeveloperManager(BaseUserManager):

    def create_user(self, email, password, firstname, lastname, date_of_birth):
        """
        Creates and save a user with the given firstname, lastname, date of birth, email and password
        :param email:
        :param password:
        :param firstname:
        :param lastname:
        :param date_of_birth:
        :return: user
        """
        if not email:
            raise ValueError('Enter an email address')
        if not password:
            raise ValueError('Enter the password')
        if not lastname:
            raise ValueError('Enter the lastname')
        if not firstname:
            raise ValueError('Enter the firstname')
        if not date_of_birth:
            raise ValueError('Enter date of birth')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            firstname=firstname,
            lastname=lastname
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, firstname, lastname, date_of_birth):
        user = self.create_user(email, password, firstname, lastname, date_of_birth)
        user.is_admin = True
        user.save(using=self._db)
        return user


class Developer(AbstractBaseUser):
    """This is the developer model class"""
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True, error_messages={'unique': 'A user with the same email already exist'})
    password = models.CharField(max_length=100)
    twitter = models.URLField(max_length=200, blank=True,)
    instagram = models.URLField(max_length=200, blank=True)
    linkedin = models.URLField(max_length=200, blank=True)
    facebook = models.URLField(max_length=200, blank=True)
    github = models.URLField(max_length=200, blank=True)
    mobile = models.CharField(max_length=11, unique=True, blank=True, null=True,
        error_messages={'unique': 'A user already registered with this mobile number'}, validators=[validate_mobile_number])
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    objects = DeveloperManager()
    # Fields required when creating a new superuser
    # REQUIRED_FIELDS must contain all required fields on your user model, but should not contain the
    # USERNAME_FIELD or password as these fields will always be prompted for.
    REQUIRED_FIELDS = ['firstname', 'lastname', 'date_of_birth'] # email and password are required by default
    USERNAME_FIELD = 'email'

    def __str__(self):
        return "{} {}".format(self.firstname, self.lastname)

    def get_full_name(self):
        return '{} {}'.format(self.firstname, self.lastname)

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    def get_username(self):
        return self.email

    @property
    def is_staff(self):
        # Is the user a member or a staff?
        # Simplest possible answer: All admins are staff
        return self.is_admin


