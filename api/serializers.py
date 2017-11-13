from rest_framework import serializers

from .models import Api


class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Api
        fields = ('title', 'description', 'completed')

    # def create(self, validated_data):
    #     validated_data['user_id'] = self.request.user_id
    #     return super(self, ApiSerializer).create(validated_data)