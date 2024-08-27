#aqui vamos a arrancar la api de google
import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
#SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]
SCOPES = ["https://www.googleapis.com/auth/calendar"]

class googleCalendarApi:
    def __init__(self):
      self.servicio = self._autenticarApi()
    """Shows basic usage of the Google Calendar API.
        Prints the start and name of the next 10 events on the user's calendar.
        """
    def _autenticarApi(self):
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("/home/amon83/CODIGOS/Python/ApiCalendarGoogle/token.json", SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file("/home/amon83/CODIGOS/Python/ApiCalendarGoogle/Packages/credentials.json", SCOPES)
                creds = flow.run_local_server(port=0)

            # Save the credentials for the next run
            with open("token.json", "w") as token:
                token.write(creds.to_json())

        
        return  build("calendar", "v3", credentials=creds)

    # Call the Calendar API
    def listarEvento(self):
        #print(self.servicio)
        hoy = datetime.datetime.today().isoformat() + "Z"  # 'Z' indicates UTC time
        print(hoy)
        tomorrow = (datetime.datetime.today() + datetime.timedelta(days=1)).replace(hour=23, minute=59,second=0,microsecond=0).isoformat() + "Z"
        print(tomorrow)
        print("Getting the upcoming 10 events")
        events_result = (
            self.servicio.events()
            .list(
                calendarId="primary",
                timeMin=hoy,
                timeMax=tomorrow,
                maxResults=10,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )
        events = events_result.get("items", [])

        if not events:
            print("No upcoming events found.")
            return

        # Prints the start and name of the next 10 events
        for event in events:
            start = event["start"].get("dateTime", event["start"].get("date"))
            print(start, event["summary"])

    def crearEvento(self,titulo,descripcion,horarioIni,horarioTer,correos:list):
       
        event = {
            'summary': titulo,
            'description': descripcion,
            'start': {
                'dateTime': horarioIni,
                'timeZone': 'Chile/Continental',
            },
            'end': {
                'dateTime': horarioTer,
                'timeZone': 'Chile/Continental',
            },
            'attendees': correos,
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'email', 'minutes': 24 * 60},
                    {'method': 'popup', 'minutes': 10},
                ],
            },
        }

        event = self.servicio.events().insert(calendarId='primary', body=event).execute()
        print(event.get('htmlLink'))
        print("Se crea el evento ok")
        return 'Se crea el evento ok'
  
#calendario = googleCalendarApi()
#titulo = "Este es el titulo"
#descripcion = "Aqui va la descripcion del evento"
#correos = [
#    {'email': 'alexis.valerio83@gmail.com'},
#    {'email': 'mandrakflax@gmail.com'},
#]
#calendario.crearEvento(titulo,descripcion,correos)
#calendario.listarEvento()