from django.urls import path,include
from rest_framework import routers
from .views import BrokerViewSet,BrokerReadOnlyViewSet

router = routers.DefaultRouter()
router.register('developer-all/',BrokerViewSet,basename="developer-all")
router.register('brokerreadonlyviewset/',BrokerReadOnlyViewSet,basename="BrokerReadOnlyViewSet")

urlpatterns = [
    path('api/', include(router.urls)),
]
