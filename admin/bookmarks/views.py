from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Bookmark
from .serializers import BookmarkSerializer, BookmarkSerializer_return

class BookmarkViewSet(viewsets.ViewSet):
    def list(self, request):
        if request.user.is_authenticated:
            bookmarks_public = Bookmark.objects.filter(status="public")
            bookmarks_private = Bookmark.objects.filter(status="private").filter(user_id=request.user.id)
            bookmarks = bookmarks_public | bookmarks_private
            serializer = BookmarkSerializer_return(bookmarks, many=True)
            return Response(serializer.data)
        else:
            bookmarks = Bookmark.objects.filter(status="public")
            serializer = BookmarkSerializer_return(bookmarks, many=True)
            return Response(serializer.data)
    
    def create(self, request):
        serializer = BookmarkSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, pk=None):
        bookmark = Bookmark.objects.get(id=pk)
        serializer = BookmarkSerializer(bookmark)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk=None):
        bookmark = Bookmark.objects.get(id=pk)
        serializer = BookmarkSerializer(instance=bookmark, data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
    def destroy(self, request, pk=None):
        bookmark = Bookmark.objects.get(id=pk)
        bookmark.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class UserAPIView(APIView):


    def create(self, serializer):
        pass