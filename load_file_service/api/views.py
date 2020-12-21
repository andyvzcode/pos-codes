from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

#____________________________________________________________________#


# Healtcheck service
@csrf_exempt
@api_view(['GET'])
def health_check(request):
    return Response({"msg": "ok"}, status=status.HTTP_200_OK)
