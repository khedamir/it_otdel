from rest_framework import serializers
from .models import Aplications, Cabinets, Frame

class AplicationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aplications
        fields = "__all__"
    author = serializers.CharField(max_length = 255)
    category = serializers.CharField()
    comment = serializers.CharField()
    date = serializers.DateField(read_only = True)
    cabinet = serializers.CharField()
    user = serializers.CharField(read_only = True)
    status = serializers.BooleanField(default = True)

    def create (self, validated_data):
        return Aplications.objects.create(**validated_data)

# class CabinetsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Cabinets
#         fields = "__all__"
#     number = serializers.IntegerField()
#     frame = serializers.CharField()

#     def create (self, validated_data):
#         return Cabinets.objects.create(**validated_data)


# class FrameSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Frame
#         fields = "__all__"
        
