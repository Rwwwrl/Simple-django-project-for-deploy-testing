from rest_framework.views import APIView
from rest_framework.response import Response

from . import models, serializers


class GetBooksView(APIView):
    def get(self, request):
        books = models.Book.objects.select_related('author').all()
        serializer = serializers.BookSerializer(books, many=True)
        return Response({'ANSWER': serializer.data})
