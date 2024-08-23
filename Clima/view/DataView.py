from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from dateutil import parser
from pandas import DataFrame, read_excel, read_csv
from django.db import transaction

from Clima.models import Daily_Indicadores
from Clima.serializers import DailyIndicadorSerializers
import pandas as pd


def df_change_types(dataframe, column_types: dict):
    for column, type in column_types.items():
        dataframe[column] = dataframe[column].astype(type)
    return dataframe

class DataView(APIView):
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):        
        Data = Daily_Indicadores.objects.filter(Activo=True).order_by('Date')
        serializer = DailyIndicadorSerializers(Data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @transaction.atomic
    def post(self, request):
        try:
            data = request.FILES['file']
        except KeyError:
            response = {
                'message': 'Debes enviar un archivo excel o CSV.'
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        # 1 
        print("data: ",data)
        extension = data.name.rpartition(".")[2].lower()
        print("extension: ",extension)
        if extension in ["ods", "xls", "xlsx"]:
            datos_clima = read_excel(data)
        elif extension == "csv":
            datos_clima = read_csv(data)
        try:
            pass    # 1
        except Exception:
            response = {
                'message': 'Tipo de archivo no válido.'
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        
        """ 
        años = datos_clima["Date"].map(lambda v: v[:4])
        porcentaje_nulos_anuales = datos_clima.isnull().groupby(años).aggregate(lambda series: sum(series)/len(series))
        for column in porcentaje_nulos_anuales.columns:
            if porcentaje_nulos_anuales[column]
        """
        variables_ambientales = [
            "Precipitation",
            "Temp_Air_Mean",
            "Temp_Air_Min",
            "Temp_Air_Max",
            "Dew_Temp_Mean",
            "Dew_Temp_Max",
            "Dew_Temp_Min",
            "Relat_Hum_Mean",
            "Relat_Hum_Min",
            "Relat_Hum_Max",
            "Wind_Speed_Mean",
            "Wind_Speed_Min",
            "Wind_Speed_Max",
            "Atmospheric_Pressure_Max",
            "Atmospheric_Pressure_Min",
        ]
        campos_requeridos = [
            "Date",
            *variables_ambientales,
        ]
        
        try:
            datos_clima = datos_clima[campos_requeridos].sort_values("Date")
        except KeyError:
            response = {
                'message': 'El archivo no contiene las columnas requeridas.',
                "required_fields": campos_requeridos,
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        
        start = datos_clima['Date'].iloc[0] 
        end = datos_clima['Date'].iloc[-1] 
        datos_clima_en_bd = Daily_Indicadores.objects.filter(
            Date__range=[parser.parse(start), parser.parse(end)], Activo=True
        )
        for dato_clime in datos_clima_en_bd:
            dato_clime.Activo = False
            dato_clime.save()
        
        for _, dato_clima in datos_clima.iterrows(): 
            dato_clima = dict(dato_clima)
            for variable in variables_ambientales:
                if pd.isna(dato_clima[variable]):
                    dato_clima[variable] = None
            serializer = DailyIndicadorSerializers(data=dato_clima)
            if serializer.is_valid():
                serializer.save()
            else:
                response = {
                    'message': 'Error al guardar registro.',
                    'errors': serializer.errors,
                    "row": dato_clima,
                }
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        response = {
            'message': 'Registros guardados correctamente.',
            "count": len(datos_clima),
        }
        return Response(response, status=status.HTTP_201_CREATED)        
        
    @transaction.atomic
    def delete(self, request):
        try:    
            start = request.GET['start']
            end = request.GET['end']
        except KeyError:
            response = {
                'message': 'Debes enviar la fecha de inicio y fin'
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        except parser.ParserError:
            response = {
                'message': 'Fecha en formato inválido'
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        recorda = Daily_Indicadores.objects.filter(
            Date__range=[parser.parse(start), parser.parse(end)], Activo=True
        )
        count = 0
        for record in recorda:
            record.Activo = False
            record.save()
            count += 1
        response = {
            'message': 'Registros eliminados',
            'count': count
        }
        return Response(response, status=status.HTTP_200_OK)
