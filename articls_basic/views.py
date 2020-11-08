from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializer import ArticlesDetailSerializer
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

""" csrf_excemption is required """
@csrf_exempt
def article_list(request):
    """ Get , Post Request """
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticlesDetailSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser(request)
        serializer = ArticlesDetailSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def articles_detailed(request, id):
    try:
        article = Article.objects.get(pk=id)
    except:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = ArticlesDetailSerializer(article)
        return JsonResponse(serializer.data, status=200,safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ArticlesDetailSerializer(article,data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=200)
        return JsonResponse(serializer.errors,status=400)

    elif request.method == 'DELETE':
        article.delete()
        return HttpResponse(status=204)