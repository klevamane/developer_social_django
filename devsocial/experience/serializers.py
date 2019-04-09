from rest_framework import serializers

from .models import Experience


class ExperienceSerializer(serializers.ModelSerializer):
    """The experience serializer class"""
    class Meta:
        fields = '__all__'
        model = Experience