from rest_framework import serializers

from diary.models import Diary


class DiaryModelSerializer(serializers.ModelSerializer):
    created_by = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Diary
        exclude = []

    # def validate(self, attrs):
    #     print(dir(self))
    #     print(self.instance.validate_unique())
    #     print(attrs)
    #     validated_data = super().validate(attrs)
    #     created_by = validated_data['created_by']
    #     print(created_by)
    #     print(validated_data)
    #     return validated_data
