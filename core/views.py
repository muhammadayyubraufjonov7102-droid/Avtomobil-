from django.shortcuts import render
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from rest_framework.generics import (CreateAPIView, 
                                     ListAPIView, RetrieveAPIView, 
                                     UpdateAPIView, DestroyAPIView)
from rest_framework.permissions import IsAuthenticated

from .models import Car
from .serializers import *


@extend_schema(
    tags="register"
)
class SignUpViews(CreateAPIView):
    serializer_class = SignUpSerializer

@extend_schema(
    tags="view-cars"
)
class CarListApiView(ListAPIView):
    serializer_class = CarListSerializers
    def get_queryset(self):
        return Car.objects.filter(user=self.request.user)
    
    
@extend_schema(
    tags="view-cars"
)    
class CarDetailApiView(RetrieveAPIView):
    serializer_class = CarDetailSerializers
    
    def get_queryset(self):
        return Car.objects.filter(user=self.request.user)
    

@extend_schema(
    tags="create-update-cars"
)   
class CarCreateApiView(CreateAPIView):
    serializer_class = CarCreateSerializers
    permission_classes = [IsAuthenticated]
    
    
    
    
    @extend_schema(
        parameters=[
        OpenApiParameter(
        name = 'car_name',
        type=OpenApiTypes.STR,
        location=OpenApiParameter.QUERY,
        description="filter by name and brand" 
        )
        ]
    )
    def get_authenticate_header(self, request):
        return super().get_authenticate_header(request)
    
    def get_queryset(self):
        queryset = Car.objects.filter(user=self.request.user)
        name = self.request.query_params.get('name')
        brand = self.request.query_params.get('brand')
        if name:
            queryset = queryset.filter(cars__name__icontains = name)
        elif brand:
            queryset = queryset.filter(cars__brand__icontains = brand)
            
        return queryset
    
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

@extend_schema(
    tags="create-update-cars"
)      
class CarUpdateApiView(UpdateAPIView):
    serializer_class = CarUpdateSerializers
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Car.objects.filter(user=self.request.user) 


@extend_schema(
    tags="delete-car"
)
class CarDeleteApiView(DestroyAPIView):
    serializer_class = CarDetailApiView
    permission_classes = [IsAuthenticated] 
    
    def get_queryset(self):
        return Car.objects.filter(user=self.request.user)




