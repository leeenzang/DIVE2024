from rest_framework import serializers
from .models import Cleanup

class CleanupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cleanup
        fields = '__all__'