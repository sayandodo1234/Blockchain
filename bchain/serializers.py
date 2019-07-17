from .models import Blockchain,Block
from rest_framework import serializers

class Blockserializer(serializers.ModelSerializer):
    class Meta:
        model=Block
        fields='__all__'