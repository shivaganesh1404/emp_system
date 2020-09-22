from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import FileSerializer
from .models import File


class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self,request):
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(serializer.errors)

    def get(self, request, format=None):
        mobile_number = request.GET.get('mobile_number')
        profile = File.objects.filter(mobile_number=mobile_number)
        serializer = FileSerializer(profile, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
