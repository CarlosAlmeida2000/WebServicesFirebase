from Persona.models import Personas
from rest_framework.views import APIView
from rest_framework.response import Response
from .correo import Correo
import json
import telegram
import asyncio

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

class vwTelegram(APIView):
    def get(self, request, format = None):
        if request.method == 'GET':
            try:
                return Response({'usuarios_bot': asyncio.run(getUsuariosBot()) })
            except Exception as e:
                return Response({'usuarios_bot': 'error '+str(e)})

    def post(self, request, format = None):
        if request.method == 'POST':
            try:
                asyncio.run(enviarChat())
                return Response({'telegram': True })
            except Exception as e: 
                return Response({'telegram': 'error '+ str(e)})  


async def getUsuariosBot():
    bot = telegram.Bot(token="6035853432:AAHU4i85YSZFSEiRJdmWFdfneVvnx_z7U4w")
    data = await bot.get_updates()
    usuarios = []

    for elemento in data:
        message = str(elemento['message'])
        if message != 'None':
            array = message.split('=')

            usuarios.append({
                "id": array[4].split(',')[0],
                "nombres": array[3].split(',')[0][1:][:-1],
                "apelludos": array[5].split(',')[0][1:][:-1],
                "usuario": array[7].split(',')[0][1:][:-2],
            })

    return usuarios


async def enviarChat():
    bot = telegram.Bot(token="6035853432:AAHU4i85YSZFSEiRJdmWFdfneVvnx_z7U4w")
    await bot.send_message(chat_id="1243290821", text="Tu pana Carlos está siendo secuestrado por las bandidas, ve a rescatarlooooo")
