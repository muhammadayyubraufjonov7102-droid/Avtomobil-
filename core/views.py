from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from rest_framework.generics import (CreateAPIView, 
                                     ListAPIView, RetrieveAPIView, 
                                     UpdateAPIView, DestroyAPIView)
from rest_framework.permissions import IsAuthenticated

from .models import Car
from .serializers import *


@extend_schema(
    tags=["register"]
)
class SignUpViews(CreateAPIView):
    serializer_class = SignUpSerializer

@extend_schema(
    tags=["view-cars"]
)
class CarListApiView(ListAPIView):
    serializer_class = CarListSerializers
    queryset =Car.objects.all()
    
    filter_backends =[DjangoFilterBackend]
    filterset_fields =['name', 'brand']
    
    
    
@extend_schema(
    tags=["view-cars"]
)    
class CarDetailApiView(RetrieveAPIView):
    serializer_class = CarDetailSerializers
    
    
    

@extend_schema(
    tags=["create-update-cars"]
)   
class CarCreateApiView(CreateAPIView):
    serializer_class = CarCreateSerializers
    permission_classes = [IsAuthenticated]
    
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

@extend_schema(
    tags=["create-update-cars"]
)      
class CarUpdateApiView(UpdateAPIView):
    serializer_class = CarUpdateSerializers
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Car.objects.filter(user=self.request.user) 


@extend_schema(
    tags=["delete-car"]
)
class CarDeleteApiView(DestroyAPIView):
    serializer_class = CarDetailSerializers
    permission_classes = [IsAuthenticated] 
    
    def get_queryset(self):
        return Car.objects.filter(user=self.request.user)




