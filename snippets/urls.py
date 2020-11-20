from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import snippet_list, snippet_detail, SnippetList, SnippetDetail,UserList,UserDetail

urlpatterns = [
    #function based view
    path('', snippet_list),
    path('<int:pk>/', snippet_detail),

    #class based view
    path('class/', SnippetList.as_view()),
    path('class/<int:pk>/', SnippetDetail.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)




