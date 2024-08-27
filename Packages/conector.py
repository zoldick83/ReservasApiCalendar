import logging
from dotenv import load_dotenv
import os

load_dotenv()
CONECTOR_LOG = os.getenv("CONECTOR_LOG")
HOST_MONGO = os.getenv("HOST_MONGO")
USER_MONGO = os.getenv("USER_MONGO")
PASS_MONGO = os.getenv("PASS_MONGO")
PUERTO_MONGO = os.getenv("PUERTO_MONGO")

logging.basicConfig(filename=CONECTOR_LOG, format='%(asctime)s %(message)s')

class  Conector:
    def __init__(self, tipoConector):
        self.tipoConector = tipoConector
        if self.tipoConector == 'MONGO':
            logging.warning('conectando a mongo')
            Conector.mongoConect()
            
    def mongoConect():
        print('coneccion realizada')
        logging.warning('conectando a mongo')
        print(f'host:  {HOST_MONGO}')
        print(f'host:  {USER_MONGO}')
        print(f'host:  {PASS_MONGO}')
        print(f'host:  {PUERTO_MONGO}')




#PARA PROBAR LAS CLASES QUE SE REALIZARAN
#db = Conector('MONGO')
