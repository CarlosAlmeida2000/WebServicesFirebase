from Persona.models import Personas
from rest_framework.views import APIView
from rest_framework.response import Response
import json

# Create your views here.
class vwPersona(APIView):
    def get(self, request, format = None):
        if request.method == 'GET':
            try:
                persona = Personas()
                return Response({'personas': persona.getData(request) })
            except Exception as e:
                return Response({'personas': 'error'})
        
    def post(self, request, format = None):
        if request.method == 'POST':
            try:
                json_data = json.loads(request.body.decode('utf-8'))
                persona = Personas()
                return Response({'personas': persona.createData(json_data) })
            except Exception as e: 
                return Response({'personas': 'error'})
    
    def put(self, request, format = None):
        if request.method == 'PUT':
            try:
                json_data = json.loads(request.body.decode('utf-8'))
                persona = Personas()
                return Response({'personas': persona.updateData(json_data) })
            except Exception as e: 
                return Response({'personas': 'error'})

    def delete(self, request, format = None):
        if request.method == 'DELETE':
            try:
                persona = Personas()
                return Response({'objetos': persona.deleteData(request)})
            except Exception as e: 
                return Response({'objetos': 'error'})