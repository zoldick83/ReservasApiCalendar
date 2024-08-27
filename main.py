from Packages.clientes import Reservas
from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
from jose import jwt, JWSError


#Inicializo la libreria FastApi
app = FastAPI()
#montar carpeta estaticas para css
app.mount("/static", StaticFiles(directory="static"),name="static")
#montar la carpeta de los template HTML
jinja2_template = Jinja2Templates(directory="templates")

#La Pagina index en donde realizaremos la Reserva
@app.get("/", response_class=HTMLResponse)
def root(request:Request):
    #return {'mensaje':'Conectando a la pagina'}
    return jinja2_template.TemplateResponse("index.html", {"request": request})

 #La Pagina index en donde realizaremos la Reserva
@app.get("/reserva")
def root():
    
    reserva1 = Reservas()
    #CrearEvento(self,titulo,descripcion,rut,fecha1,fecha2,hora1,hora2):
    salida = reserva1.CrearEvento('titulo desde el front','cualquier cosa','15548355-5','2024-07-30','2024-07-30','09:00:00','10:00:00')
    #salida = reserva1.BuscarCorreoUser(db_correos,'15548355-5')
    return salida
    #return jinja2_template.TemplateResponse("index.html", {"request": request})   