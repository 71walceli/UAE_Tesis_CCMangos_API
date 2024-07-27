from rest_framework import routers
from django.urls import path, re_path
from Hacienda.views import (
    LoteAPIView,
    AreaAPIView,
    ProyectoHaciendaAPIView,
    GeoLotesView,
    EnfermedadAPIView,
    VariedadAPIView,
    LecturaAPIView,
    PlantaAPIView,
    ProduccionAPIView,
    PlantasFotosView,
    VerificarExistenciaAPIView,
    PredictiveApiView, PREDICTIONS_ENDPOINT,
)
from Hacienda.api import HaciendaViewSet, ProyectoViewSet


router = routers.DefaultRouter()
router.register('api/hacienda', HaciendaViewSet)
router.register('api/proyectos', ProyectoViewSet)
urlpatterns = [
    path('api/hacienda/<int:hacienda_id>/proyectos/', ProyectoHaciendaAPIView.as_view(), name='proyectos-hacienda'),
    path('api/areas/', AreaAPIView.as_view(), name='lotes'),
    path('api/areas/<int:id_lotes>/', AreaAPIView.as_view(), name='lotes'),
    path('api/lotes/', LoteAPIView.as_view(), name='lotes'),
    path('api/lotes/<int:id_proyecto>/', LoteAPIView.as_view(), name='lotes'),
    path('api/geolotes/', GeoLotesView.as_view(), name='geolotes'),
    path('api/geolotes/<int:lote_id>/', GeoLotesView.as_view(), name='geolotes'),
    path('api/enfermedades/', EnfermedadAPIView.as_view(), name='lecturas'),
    path('api/variedades/', VariedadAPIView.as_view(), name='lecturas'),
    path('api/lecturas/', LecturaAPIView.as_view(), name='lecturas'),
    path('api/plantas/', PlantaAPIView.as_view(), name='plantas'),
    path('api/plantas/fotos/upload/', PlantasFotosView.as_view(), name='PlantasFotosView'),
    path('api/produccion/', ProduccionAPIView.as_view(), name='produccion'),
    path("api/misc/verificar_existencia", VerificarExistenciaAPIView.as_view()),
    #path(f"api{PREDICTIONS_ENDPOINT}", PredictiveApiView.as_view()),
    re_path(rf'^api/{PREDICTIONS_ENDPOINT}/(?P<subpath>.*)$', PredictiveApiView.as_view()),

]
urlpatterns += router.urls
