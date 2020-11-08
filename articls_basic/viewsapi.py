from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Article
from .serializerModel import ArticlesSerializer
from rest_framework import status

class ArticleApiView(APIView):
    def get(self, request):
        article = Article.objects.all()
        serializer = ArticlesSerializer(article,many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = ArticlesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)



class ArticleDetailApiView(APIView):
    def get_object(self,id):
        try:
            article = Article.objects.get(pk=id)
            return article
        except:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self,request, id):
        article = self.get_object(id)
        serializer = ArticlesSerializer(article)
        return Response(serializer.data,status.HTTP_202_ACCEPTED)

    def put(self,request, id):
        serializer = ArticlesSerializer(self.get_object(id),request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        self.get_object(id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

