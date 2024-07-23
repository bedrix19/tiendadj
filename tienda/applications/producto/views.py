from django.shortcuts import render
from rest_framework.generics import(
    ListAPIView,
)

from . serializers import ProductSerializer

from .models import Product

# Create your views here.

class ListProductUser(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()