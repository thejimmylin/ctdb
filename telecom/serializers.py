from rest_framework import serializers
from .models import PrefixListUpdateTask


class PrefixListUpdateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrefixListUpdateTask
        fields = '__all__'
