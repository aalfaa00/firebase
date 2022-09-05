from rest_framework import serializers
from .models import UserToken



class UserTokenSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserToken
        fields = '__all__'




class UserMessageSerializers(serializers.Serializer):
    message = serializers.CharField(max_length=500)