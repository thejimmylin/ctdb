from rest_framework import serializers

from diary.models import Diary


class DiaryModelSerializer(serializers.ModelSerializer):
    created_by = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Diary
        exclude = []
