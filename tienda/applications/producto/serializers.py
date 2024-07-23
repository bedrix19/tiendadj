from rest_framework import serializers

from .models import Product

# Create your views here.

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = {
            'name',
            'description',
            'man',
            'woman',
        }
