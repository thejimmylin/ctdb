from rest_framework import serializers

from diary.models import Diary


class DiaryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        exclude = ['created_by']

    # def validate(self, instance):
    #     super().validate()
    #     try:
    #         instance.validate_unique()
    #     except forms.ValidationError:
    #         self.add_error(field='date', error=_('The diary with this date has already existed.'))
