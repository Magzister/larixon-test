from rest_framework import serializers
from .models import Advert


class AdvertAttributeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)

class AdvertSerializer(serializers.ModelSerializer):
    city = AdvertAttributeSerializer(many=False)
    categories = AdvertAttributeSerializer(many=True)
    class Meta:
        model = Advert
        fields = ['id', 'title', 'description', 'views', 'city', 'categories']
