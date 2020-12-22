from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ParseError
from django.core.files.storage import FileSystemStorage
import requests
import os
#____________________________________________________________________#


# Healtcheck service
@csrf_exempt
@api_view(['GET'])
def health_check(request):
    return Response({"msg": "ok"}, status=status.HTTP_200_OK)


class FileUploadView(APIView):
    ALLOWED_EXTENSIONS = ["csv"]
    FOLDER = 'files/'

    def post(self, request, format=None):
        if 'file' not in request.data or request.data['file'] == "" or request.data.get("file") == None or 'file' not in request.FILES:
            raise ParseError("Not File Provider")

        file = request.FILES['file']
        file_extension = file.name.split('.')[1]
        if file_extension in self.ALLOWED_EXTENSIONS:
            fs = FileSystemStorage(location=self.FOLDER)
            filename = fs.save(file.name, file)
            process_file(filename)
            return Response({
                "msg": "File Process"
            }, status=200)
        else:
            return Response({
                "msg": "Archivo no permitido"
            }, status=400)


def process_file(file):
    api_url = os.environ.get("API_PROCESS_FILE")
    file_url = 'files/'+file
    body = {"file": (file_url, open(file_url, 'rb'))}
    data = {'dir': '/uploads/', 'submit': 'Submit'}

    r = requests.post(url=api_url, files=body, data=data)
    print(r)
    return {"ok": "ok"}
