"""other imports """

""" Djnago imports"""

"""rest api viewset(get,update,delete,retrive)"""
from rest_framework import viewsets

""" Rest-api Security """
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication,BasicAuthentication,TokenAuthentication

""" Serilizer imports """
from .serializer import UserSerializer

""" Custom user model import """
from .models import User

class BrokerViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_broker=True)
    serializer_class = UserSerializer
    pagination_class = None
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

class BrokerReadOnlyViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_broker=True)
    serializer_class = UserSerializer
    pagination_class = None
