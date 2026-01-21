from rest_framework import serializers
from .models import Car, User
from .exception import CustomValidationError



class SignUpSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    def create(self, validated_data):
        username = validated_data["username"]
        password = validated_data["password"]
        user = User.objects.create(username=username)
        user.set_password(password)
        user.save()
        return user
    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            raise CustomValidationError("Username already exist!!!")
        return username
    

class CarListSerializers(serializers.models):
    egasi = serializers.SerializerMethodField()
    class Meta:
        model = Car
        fields = ['id', 'name', 'brand', 'year', 'mileage', 'engine_power', 'price', 'user', 'egasi']
        
        def get_egasi(self, obj):
            return f"{obj.user.name} {obj.user.phone_number}"
        


class CarDetailSerializers(serializers.models):
    egasi = serializers.SerializerMethodField()
    class Meta:
        model = Car
        fields = ['id', 'name', 'brand', 'year', 'mileage', 'engine_power', 'price', 'user', 'egasi']
        
        def get_egasi(self, obj):
            return f"{obj.user.User.name} {obj.user.User.phone_number}"
        
        
class CarCreateSerializers(serializers.models):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Car
        fields = ['id', 'name', 'brand', 'year', 'mileage', 'engine_power', 'price', 'user']
        


class CarUpdateSerializers(serializers.models):
    class Meta:
        model = Car
        fields = ['id', 'name', 'brand', 'year', 'mileage', 'engine_power', 'price', 'user']


