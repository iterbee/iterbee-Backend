from rest_framework import serializers
from .models import CulturalPoint

class CulturalPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = CulturalPoint
        fields = ["coord", "location_name", "info"]