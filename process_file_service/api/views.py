from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import PosCodes
import csv
import io
import requests
import os
#____________________________________________________________________#


# Healtcheck service
@csrf_exempt
@api_view(['GET'])
def health_check(request):
    return Response({"msg": "ok"}, status=status.HTTP_200_OK)


class ProcessFileView(APIView):
    def post(self, request, format=None):
        csv_file = request.FILES['file']
        data_set = csv_file.read().decode('UTF-8')
        lines = data_set.split("\n")
        del lines[0]
        for line in lines:
            fields = line.split(",")
            if len(fields) == 2:
                payload = {"lon": fields[1], "lat": fields[0]}
                r = requests.get(os.environ.get(
                    "API_POS_CODES"), params=payload)
                response = r.json()
                code = response['result'][0]['postcode'] if response['result'] is not None else None
                reg = PosCodes.objects.create(
                    code=code, lat=fields[0], lng=fields[1])
        return Response({
            "msg": "File Process"
        }, status=200)
