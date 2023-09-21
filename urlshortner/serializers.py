from rest_framework import serializers

class CreateShortURISerializer(serializers.Serializer):
    originalURI = serializers.CharField()
    expireDay = serializers.IntegerField()

    def validate(self, data):

        return data

class UpdateShortURISerializer(serializers.Serializer):
    originalURI = serializers.CharField()
    shortURI = serializers.CharField()

    def validate(self, data):

        return data

class UpdateExpirySerializer(serializers.Serializer):
    shortURI = serializers.CharField()
    expireDay = serializers.IntegerField()

    def validate(self, data):
        return data