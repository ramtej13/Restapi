from rest_framework import viewsets
from .models import Article
from .serializerModel import ArticlesSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status

class ArticleViewset(viewsets.ViewSet):
    def list(self, request):
        queryset = Article.objects.all()
        serializer = ArticlesSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = request.objects.all()
        article = get_object_or_404(queryset, pk=pk)
        serializer = ArticlesSerializer(article)
        return Response(serializer.data)

    def create(self, request):
        serilizer = ArticlesSerializer(request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data, status.HTTP_200_OK)
        return Response(serilizer.errors,status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        queryset = request.objects.all()
        articl = get_object_or_404(queryset,pk=pk)
        serilizer = ArticlesSerializer(articl,request.data)
        serilizer.save()

    # def delete(self,request,pk=None):

