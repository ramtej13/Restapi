from .viewsapi import ArticleApiView,ArticleDetailApiView
from django.urls import path,include
from .viewsgeneric import ArticlesGenericView,ArticlesDetailGenericView
from rest_framework import routers
from .viewsviewset import ArticleViewset

router = routers.DefaultRouter()
router.register('viesetArticle',ArticleViewset,basename="ArticleViewset")


urlpatterns = [
    # normal view
    # path('',article_list),
    # path('<id>',articles_detailed)

    #api view
    path('',ArticleApiView.as_view()),
    path('<id>',ArticleDetailApiView.as_view()),

    # generic Api view
    path('gen/',ArticlesGenericView.as_view()),
    path('gen/<id>/', ArticlesDetailGenericView.as_view()),


    path('sss/',include(router.urls)),

]