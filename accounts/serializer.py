from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("email", "password",'id','is_broker')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    # def create(self, validated_data):
    #     is_broker= validated_data.pop('is_broker')
    #     user = get_user_model().objects.create_user(**validated_data)
    #     user.is_broker = is_broker
    #     user.save()
    #     return user