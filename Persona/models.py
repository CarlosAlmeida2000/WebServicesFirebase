# Cosumo del servicio sin credenciales de autenticación - FORMA # 1 ---------------------------------------------------------------------------------------------------------
""" from firebase import firebase
firebase = firebase.FirebaseApplication('https://locationuber2022-default-rtdb.firebaseio.com/', None)
 """
# FORMA # 1 ---------------------------------------------------------------------------------------------------------
""" class Personas:
    
    def getData(self, request):
        try:
            if 'id' in request.GET:
                data = firebase.get('/Uber/Personas', request.GET['id'])
                return data if data != None else {}
            data = firebase.get('/Uber/Personas', '')
            return data if data != None else {}
        except Exception as e:
            return {}
        

    def createData(self, data):
        try:            
            result = firebase.post('/Uber/Personas', data)
            return (result != None)
        except Exception as e:
            return False

    def updateData(self, data):
        try:
            result = firebase.put('/Uber/Personas/', data['id'], data)
            return (result != None)
        except Exception as e:
            return False

    def deleteData(self, request):
        try:
            firebase.delete('/Uber/Personas/', request.GET['id'])
            return True
        except Exception as e:
            return False
 """








# Cosumo del servicio con credenciales de autenticación - FORMA # 2 ---------------------------------------------------------------------------------------------------------
# Importaciones con la FORMA # 2 ---------------------------------------------------------------------------------------------------------
# Importo Firebase Admin SDK 
import firebase_admin
# Hacemos uso de credenciales que nos permitirán usar Firebase Admin SDK 
from firebase_admin import credentials
# Importo el Servicio Firebase Realtime Database 
from firebase_admin import db


# FORMA # 2 ---------------------------------------------------------------------------------------------------------
class RealTimeDatabase:

    @staticmethod
    def openConnection ():
        try:
            # Llamo al archivo JSON que contiene mi clave privada 
            cred = credentials.Certificate('./locationuber2022-firebase-adminsdk-2oz3x-7070bdca01.json')
        
            # Iniciamos los servicios de Firebase con las credenciales y el nombre de mi proyecto en Firebase 
            firebase_admin.initialize_app(cred, {
                'databaseURL': 'https://locationuber2022-default-rtdb.firebaseio.com/'
            })
            return True
        except Exception as e:
            return False

    @staticmethod
    def closeConnection():
        try:
            firebase_admin.delete_app(firebase_admin.get_app())
            return True
        except Exception as e:
            return False



class Personas:
     
    def getData(self, request):

        if(RealTimeDatabase.openConnection()):

            if 'id' in request.GET:
                ref = db.reference('/Uber/Personas/'+ request.GET['id']) 
                datos = ref.get()
                RealTimeDatabase.closeConnection()
                return datos if datos != None else {}

            elif 'nombres' in request.GET:
                ref = db.reference('/Uber/Personas') 
                datos = ref.order_by_child('nombres').equal_to(request.GET['nombres']).get()
                RealTimeDatabase.closeConnection()
                return datos if datos != None else {}
            elif 'apellidos' in request.GET:
                ref = db.reference('/Uber/Personas') 
                datos = ref.order_by_child('apellidos').start_at(request.GET['apellidos']).end_at(request.GET['apellidos'] + '\uf8ff').get()
                RealTimeDatabase.closeConnection()
                return datos if datos != None else {}

            ref = db.reference('/Uber/Personas') 
            datos = ref.order_by_key().get()
            RealTimeDatabase.closeConnection()
            return datos if datos != None else {}


    def create(self, data):

        if(RealTimeDatabase.openConnection()):
            
            ref = db.reference('/Uber/Personas')  
            new_ref = ref.push().key
            data['id'] = new_ref
            ref.child(new_ref).set(data)

            RealTimeDatabase.closeConnection()

            return True

        return False

    def update(self, data):

        if(RealTimeDatabase.openConnection()):
            
            ref = db.reference('/Uber/Personas/'+ data['id'])

            ref.set(data)

            RealTimeDatabase.closeConnection()

            return True

        return False 

    
    def delete(self, id):

        if(RealTimeDatabase.openConnection()):
            
            ref = db.reference('/Uber/Personas')

            ref.child(id).delete()

            RealTimeDatabase.closeConnection()

            return True

        return False 