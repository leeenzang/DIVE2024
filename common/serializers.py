from rest_framework import serializers
from .models import Coastline

class CoastlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coastline
        fields = ['name', 'alias_names']