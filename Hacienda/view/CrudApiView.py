from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated


class CrudApiView(APIView):
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def __init__(self, model, serializer, parents=None):
        if not parents:
            parents = []
        self.parents = parents
        super(APIView)
        self.model = model
        self.serializer = serializer
    
    def serialize_out(self, objects, many=True):
        return self.serializer(objects, many=many).data
    
    def get_object(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            raise None
    
    def get(self, request, *args, **kwargs):
        filters = kwargs.get("filters", {})
        many = kwargs.get("many", True)
        objects = self.model.objects.filter(Activo=True, **filters)
        for predicate in (f'{"__".join(l for l in self.parents[0:i])}__Activo'
            for i in range(1, len(self.parents)+1)
        ): 
            objects = objects.exclude(**{predicate: False})
        return Response(self.serialize_out(objects, many=many))

    def post(self, request, data=None, *args, **kwargs):
        if not data:
            data = request.data
        serialized_object = self.serializer(data=data)
        if serialized_object.is_valid():
            serialized_object.save()
            return Response(serialized_object.data, status=status.HTTP_200_OK)
        else:
            return Response(serialized_object.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, data=None, *args, **kwargs):
        if data is None:
            data = request.data
        id = data.get("id")
        if not id:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        object = self.get_object(id)
        if not object:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serialized_object = self.serializer(object, data=data, partial=True)
        if serialized_object.is_valid():
            serialized_object.save()
            return Response(serialized_object.data)
        return Response(serialized_object.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete (self, request, *args, **kwargs):
        id = request.GET.get("id")
        if not id:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        object = self.get_object(id)
        if not object:
            return Response(status=status.HTTP_404_NOT_FOUND)
        object.Activo = False
        object.save()

        serialized_object = self.serializer(object)
        return Response(serialized_object.data)
