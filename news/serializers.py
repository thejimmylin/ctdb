from rest_framework import serializers

from .models import News


class NewsModelSerializer(serializers.ModelSerializer):
    created_by = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = News
        exclude = []
