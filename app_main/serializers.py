from rest_framework import serializers
from .models import User


# OopCompanion:suppressRename


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class RoleSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    permissions = serializers.ListField(child=serializers.IntegerField())