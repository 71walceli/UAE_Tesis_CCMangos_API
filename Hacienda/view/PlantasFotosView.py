from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import FileUploadParser, MultiPartParser

from ..models import PlantaFoto


class PlantasFotosView(APIView):
    parser_classes = (MultiPartParser, )

    def put(self, request):
        file = request.FILES.get("file")
        if not file:
            return Response(status=400)
        print("file: ",vars(file))
        instance = PlantaFoto(uri=file)
        instance.save()
        return Response(status=204)
