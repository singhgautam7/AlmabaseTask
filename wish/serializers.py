from rest_framework import serializers


class WishMeResponse(serializers.Serializer):

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    message = serializers.CharField(help_text='A happy birthday text message', min_length=15)
