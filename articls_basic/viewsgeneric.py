from rest_framework import generics
from rest_framework import mixins
from .serializerModel import ArticlesSerializer
from .models import Article


class ArticlesGenericView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticlesSerializer
    """ in order query a specific dataset use lookup in that queryset"""

    def get(self, request):
        return self.list(request)

    def post(self,request):
        return self.create(request)

class ArticlesDetailGenericView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                          mixins.UpdateModelMixin,mixins.DestroyModelMixin,mixins.RetrieveModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticlesSerializer
    """ in order query a specific dataset use lookup in that queryset"""
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def put(self,request,id=None):
        return self.update(request,id)

    def delete(self,request,id=None):
        return self.destroy(request,id)