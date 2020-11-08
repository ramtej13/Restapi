from rest_framework import serializers
from .models import Article

class ArticlesDetailSerializer(serializers.Serializer):
    titel = serializers.CharField(max_length=100)
    discription = serializers.CharField(max_length=250)
    auther = serializers.CharField(max_length=50)
    email = serializers.EmailField(max_length=200)
    data = serializers.DateTimeField(auto_now_add=True)

    def create(self, validated_data):
        return Article.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("titel",instance.title)
        instance.discription = validated_data.get("titel", instance.discription)
        instance.auther = validated_data.get("titel", instance.auther)
        instance.email = validated_data.get("titel", instance.email)
        instance.data = validated_data.get("titel", instance.data)
        instance.save()
        return instance

