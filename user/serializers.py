from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the users object"""

    class Meta:
        model = User
        fields = ('username', 'email', 'password', )
        extra_kwargs = {'password': {'write_only': True, 'min_length': 6}}

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        username = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.get('password')
        user = User.objects.create_user(username, email, password)
        return user
