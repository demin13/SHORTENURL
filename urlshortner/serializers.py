from rest_framework import serializers
from .models import URLStore


class GetAllDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = URLStore
        fields = '__all__'



class CreateShortURISerializer(serializers.Serializer):
    originalUrl = serializers.CharField()
    expiryDate = serializers.DateField()

    def validate(self, data):

        return data

class UpdateShortURISerializer(serializers.Serializer):
    originalURI = serializers.CharField()
    shortURI = serializers.CharField()

    def validate(self, data):

        return data

class UpdateExpirySerializer(serializers.Serializer):
    shortURI = serializers.CharField()
    expiryDate = serializers.IntegerField()

    def validate(self, data):
        return data