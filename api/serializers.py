from rest_framework import serializers

from diary.models import Diary


class DiaryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = '__all__'
