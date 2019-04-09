from rest_framework import serializers
from .models import Education


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Education