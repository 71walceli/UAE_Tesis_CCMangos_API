from Hacienda.models import Lote, Area
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Hacienda.serializers import LoteSerializers
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

class LoteAPIView(APIView):
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    # Código existente...
    def get(self, request,*args, **kwargs):
        id_proyecto = self.kwargs.get('id_proyecto')
        if id_proyecto: 
            lotes = Lote.objects.filter(Id_Proyecto = id_proyecto, Activo=True)
        else:
            lotes = Lote.objects.filter(Activo=True)
        serializer = LoteSerializers(lotes, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = LoteSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, pk):
        lote = self.get_object(pk)
        serializer = LoteSerializers(lote, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        try:
            return Lote.objects.get(pk=pk)
        except Lote.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def delete(self, request, id):
        lote = self.get_object(id)
        lote.Activo = False
        lote.save()

        serializer = LoteSerializers(lote)
        return Response(serializer.data)
