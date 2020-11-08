from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializerModel import ArticlesSerializer
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
""" csrf_excemption is required """
@api_view(['GET','POST'])
def article_list(request):
    """ Get , Post Request """
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticlesSerializer(articles, many=True)
        return Response(serializer.data, status.HTTP_202_ACCEPTED)

    elif request.method == 'POST':
        serializer = ArticlesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def articles_detailed(request, id):
    try:
        article = Article.objects.get(pk=id)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ArticlesSerializer(article)
        return Response(serializer.data, status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = ArticlesSerializer(article,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_200_OK)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        article.delete()
        return HttpResponse(status.HTTP_202_ACCEPTED)