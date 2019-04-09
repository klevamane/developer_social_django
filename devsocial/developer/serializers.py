from rest_framework import serializers
from .models import Developer

# serializers allows complex data structures like queryset and models to be converted into native
# python data types that can be easily rendered into json, XML etc


class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Developer
