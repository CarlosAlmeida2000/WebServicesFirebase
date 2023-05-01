# Importo Firebase Admin SDK 
import firebase_admin
# Hacemos uso de credenciales que nos permitirán usar Firebase Admin SDK 
from firebase_admin import credentials

class RealTimeDatabase:

    def __init__(self) -> None:
        self.cred = None
    
    def openConnection (self):
        try:
            if( self.cred == None):
                # Llamo al archivo JSON que contiene mi clave privada 
                self.cred = credentials.Certificate('./locationuber2022-firebase-adminsdk-2oz3x-7070bdca01.json')
            
                # Iniciamos los servicios de Firebase con las credenciales y el nombre de mi proyecto en Firebase 
                firebase_admin.initialize_app(self.cred, {
                    'databaseURL': 'https://locationuber2022-default-rtdb.firebaseio.com/'
                })
            return True
        except Exception as e:
            return False

    def closeConnection(self):
        try:
            firebase_admin.delete_app(firebase_admin.get_app())
            return True
        except Exception as e:
            return False