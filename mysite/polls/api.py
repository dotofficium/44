from .models import Email

from .serializers import EmailSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class EmailList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        emails = Email.objects.all()
        serializer = EmailSerializer(emails, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
