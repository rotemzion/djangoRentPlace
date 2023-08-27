from .models import ItemLocation, UserP
from rest_framework import serializers


class ItemLocationSerializers(serializers.ModelSerializer):

    class Meta:
        model = ItemLocation
        fields = "__all__"


class UserPSerializers(serializers.ModelSerializer):

     class Meta:
        model = UserP
        fields = "__all__"
