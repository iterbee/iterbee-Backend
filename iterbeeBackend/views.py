from rest_framework import viewsets
from .models import CulturalPoint
from .serializers import CulturalPointSerializer

# Create your views here.

class CulturalPointViewSet(viewsets.ModelViewSet):
    queryset = CulturalPoint.objects.all()
    serializer_class = CulturalPointSerializer

