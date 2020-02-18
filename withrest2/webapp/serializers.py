from rest_framework import serializers


class NameSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=20)
