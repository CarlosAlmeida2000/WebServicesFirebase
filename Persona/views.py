from Persona.models import Personas
from rest_framework.views import APIView
from rest_framework.response import Response
from .correo import Correo
import json

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
                return Response({'personas': persona.create(json_data) })
            except Exception as e: 
                return Response({'personas': 'error'})
    
    def put(self, request, format = None):
        if request.method == 'PUT':
            try:
                json_data = json.loads(request.body.decode('utf-8'))
                persona = Personas()
                return Response({'personas': persona.update(json_data) })
            except Exception as e: 
                return Response({'personas': 'error'})

    def delete(self, request, format = None):
        if request.method == 'DELETE':
            try:
                persona = Personas()
                return Response({'objetos': persona.delete(request.GET['id'])})
            except Exception as e: 
                return Response({'objetos': 'error'})

class vwCorreo(APIView):
    def post(self, request, format = None):
        if request.method == 'POST':
            try:
                unCorreo = Correo()
                context = {"mensaje": "Saludos coordiales estimado", "linea2": "Motivo", "linea3": "Su cupo ha sido aceptado"}                
                if unCorreo.send("ca884012@gmail.com", "NOTIFICACIÓN", "components/correo.html", context):
                    return Response({'correo': True })
                return Response({'correo': False })
            except Exception as e: 
                return Response({'correo': 'error'})  