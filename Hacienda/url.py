from rest_framework import routers
from django.urls import path
from Hacienda.views import (LoteAPIView,
                            AreaAPIView,
                            ProyectoHaciendaAPIView,
                            GeoLotesView,
                            EnfermedadAPIView,
                            LecturaAPIView,
                            PlantaAPIView,
                            ImportLecturas,
                            ProduccionAPIView,
                            ImportProduccion,
                            ImportLotesView,
                            ImportPlantasView,
                            PlantasFotosView
                        )
from Hacienda.api import HaciendaViewSet, ProyectoViewSet#, LecturaViewSet
router = routers.DefaultRouter()
router.register('api/hacienda', HaciendaViewSet)
router.register('api/proyectos', ProyectoViewSet)
#router.register('api/lecturas', LecturaViewSet)
urlpatterns = [
    path('api/hacienda/<int:hacienda_id>/proyectos/', ProyectoHaciendaAPIView.as_view(), name='proyectos-hacienda'),
    path('api/areas/', AreaAPIView.as_view(), name='lotes'),
    path('api/areas/<int:id_lotes>/', AreaAPIView.as_view(), name='lotes'),
    path('api/lotes/', LoteAPIView.as_view(), name='lotes'),
    path('api/lotes/upload', ImportLotesView.as_view(), name='lotes'),
    path('api/lotes/<int:id_proyecto>/', LoteAPIView.as_view(), name='lotes'),
    path('api/geolotes/', GeoLotesView.as_view(), name='geolotes'),
    path('api/geolotes/<int:lote_id>/', GeoLotesView.as_view(), name='geolotes'),
    path('api/enfermedades/', EnfermedadAPIView.as_view(), name='lecturas'),
    path('api/lecturas/', LecturaAPIView.as_view(), name='lecturas'),
    path('api/lecturas/upload', ImportLecturas.as_view(), name='lecturas'),
    path('api/plantas/', PlantaAPIView.as_view(), name='plantas'),
    path('api/plantas/fotos/upload/', PlantasFotosView.as_view(), name='PlantasFotosView'),
    path('api/plantas/upload', ImportPlantasView.as_view(), name='plantas'),
    path('api/produccion/', ProduccionAPIView.as_view(), name='produccion'),
    path('api/produccion/upload', ImportProduccion.as_view(), name='Produccion'),
]
urlpatterns += router.urls
