from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import csv
import io

#____________________________________________________________________#


# Healtcheck service
@csrf_exempt
@api_view(['GET'])
def health_check(request):
    return Response({"msg": "ok"}, status=status.HTTP_200_OK)


class ProcessFileView(APIView):
    def post(self, request, format=None):
        print(request.FILES['file'])
        csv_file = request.FILES['file']
        data_set = csv_file.read().decode('UTF-8')
        lines = data_set.split("\n")
        data = []
        for line in lines:
            fields = line.split(",")
            if len(fields) == 2:
                data_dict = {}
                data_dict["lat"] = fields[0] if fields[0] != None else None
                data_dict["lng"] = fields[1] if fields[1] != None else None
                data.append(data_dict)
        print(data)


        return Response({
            "msg": "File Process"
        }, status=200)
