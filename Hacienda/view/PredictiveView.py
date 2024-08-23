import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.decorators import login_required
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from Hacienda import ENDPOINT


EXTERNAL_API_URL = "http://predictive-api:8000"
PREDICTIONS_ENDPOINT = "predicciones"

@method_decorator([csrf_exempt], name='dispatch')
class PredictiveApiView(View):
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def do_request(self, method, request): 
        trimmed = f'/{ENDPOINT}/{PREDICTIONS_ENDPOINT}'
        external_api_url = f"{EXTERNAL_API_URL}/{request.path.replace(trimmed, '')}"
        
        response = requests.request(method, external_api_url, data=request.body, 
            headers={'Content-Type': request.content_type}  
        )
        return JsonResponse(response.json(), status=response.status_code, safe=False) 

    def get(self, request, *args, **kwargs):
        return self.do_request("GET", request)

    def post(self, request, *args, **kwargs):
        return self.do_request("POST", request)
    
    def put(self, request, *args, **kwargs):
        return self.do_request("PUT", request)

    def delete(self, request, *args, **kwargs):
        return self.do_request("DELETE", request)
