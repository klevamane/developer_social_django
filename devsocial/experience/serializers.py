from rest_framework import serializers

from .models import Experience


class ExperienceSerializer(serializers.ModelSerializer):
    """The experience serializer class"""
    class Meta:
        model = Experience
        fields = '__all__'