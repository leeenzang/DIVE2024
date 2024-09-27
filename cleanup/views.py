from rest_framework import viewsets
from .models import Cleanup
from .serializers import CleanupSerializer

class CleanupViewSet(viewsets.ModelViewSet):
    queryset = Cleanup.objects.all()
    serializer_class = CleanupSerializer