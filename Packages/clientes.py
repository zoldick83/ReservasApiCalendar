#se requiere importa apy de google que esta en otro package
from Packages.calendarApi import googleCalendarApi
#Se va a crear un connector que permita insertar datos en mongo DB o en algun otro medio como excel.
from Packages.conector import Conector

db_correos = {
    '15548355-5':{'nombre':'Alexis Valerio',
                  'email':'mandrakflax@gmail.com'
                  },
    '15364449-7':{
                  'nombre':'Alexis Valerio',
                  'email':'mandrakflax@gmail.com'
                  }     
}

class Reservas:
    def __init__(self):
        print('Comenzando paquete de reservas')
        

    def CrearEvento(self,titulo,descripcion,rut,fecha1,fecha2,hora1,hora2):
        #print('Aqui se creara el evento')
        #aqui vamos a guarda el evento en base de datos
        #buscar Correo 
        correos = self.BuscarCorreoUser(db_correos, rut)
        if not correos:
             return 'Uusuario no existe'             
        #correos = [
          #  {'email': 'alexis.valerio83@gmail.com'},
         #   {'email': 'mandrakflax@gmail.com'},
        #]

        ArmandoFechaHoraIni = fecha1 +'T'+ hora1+'-04:00'
        ArmandoFechaHoraTer = fecha2 +'T'+ hora2+'-04:00'
        evento = googleCalendarApi();
        salida = evento.crearEvento(titulo,descripcion,ArmandoFechaHoraIni,ArmandoFechaHoraTer,correos)
        print(salida)
        return salida

    def ActualizarEvento():
        print('Aqui se va actualizar el evento')

    def ConsultarCalendario():
        print('aqui se podra revisar los eventos')
    
    def BuscarCorreoUser(self,correos:list, user:str):
           for lista in correos:
                if user in lista:
                    datosUser = correos[lista]
                    salida = [{'email':datosUser['email']}]
                    return salida
                return False




#PROBAR CLASES
#reserva1 = Reservas()
#print(reserva1.BuscarCorreoUser(db_correos,'15548355-5'))
#reserva1.CrearEvento()