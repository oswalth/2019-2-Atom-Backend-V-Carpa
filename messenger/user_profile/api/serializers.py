from rest_framework import serializers
from user_profile.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'last_name', 'first_name', 'username', 'password', 'avatar')

    def create(self, validated_data):
        password = validated_data.get('password', None)
        if password is not None:
            validated_data.pop('password')
            user = User(**validated_data)
            user.set_password(password)
            user.save()
            return user