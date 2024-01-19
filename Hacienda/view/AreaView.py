from Hacienda.models import Area
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Hacienda.serializers import AreaSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

class AreaAPIView(APIView):
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    # Código existente...
    def get(self, request,*args, **kwargs):
        id = self.kwargs.get('id_lotes')
        if id: 
            areas = Area.objects.filter(Id_Lote = id, Activo=True)
        else:
            areas = Area.objects.filter(Activo=True)
        serializer = AreaSerializer(areas, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = AreaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, pk):
        area = self.get_object(pk)
        serializer = AreaSerializer(area, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        try:
            return Area.objects.get(pk=pk)
        except Area.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def delete (self, request, id):
        area = self.get_object(id)
        Area.Activo = False
        Area.save()

        serializer = AreaSerializer(area)
        return Response(serializer.data)