from .viewsapi import ArticleApiView,ArticleDetailApiView
from django.urls import path
from .viewsgeneric import ArticlesGenericView,ArticlesDetailGenericView


urlpatterns = [
    # normal view
    # path('',article_list),
    # path('<id>',articles_detailed)

    #api view
    path('',ArticleApiView.as_view()),
    path('<id>',ArticleDetailApiView.as_view()),

    # generic Api view
    path('gen/',ArticlesGenericView.as_view()),
    path('gen/<id>/', ArticlesDetailGenericView.as_view())

]