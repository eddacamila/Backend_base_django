from django.contrib import admin
from django.urls import path
from .views import BookmarkViewSet

urlpatterns = [
    path('bookmarks', BookmarkViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('bookmarks/<str:pk>', BookmarkViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'    
    }))
]
