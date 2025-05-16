import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = "1bD8-MspxdauEZbcoCQz6y67kWLeVgdcP-yEhjiqpjRg"

class BuscarAmbientes:
  
  def __init__(self, nome_aba):
    self.SHEET_NAME = nome_aba
    pass
  
  def getCredencial():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    
    if os.path.exists("ApiGoogle/token.json"):
      creds = Credentials.from_authorized_user_file("ApiGoogle/token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
      if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
      else:
        flow = InstalledAppFlow.from_client_secrets_file(
            "ApiGoogle/credentials.json", SCOPES
        )
        creds = flow.run_local_server(port=0)
      # Save the credentials for the next run
      with open("ApiGoogle/token.json", "w") as token:
        token.write(creds.to_json())
    return creds

  def buscaAmbientes(self):
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = self.getCredencial()

    try:
      service = build("sheets", "v4", credentials=creds)
      
      header_result = (
        service.spreadsheets()
        .values()
        .get(spreadsheetId=SPREADSHEET_ID, range=f"{self.SHEET_NAME}!1:1")
        .execute()
      )
      values = header_result.get("values", [[]])[0]

      if not values:
        print("No data found.")
        return
      
      if "Nome do Ambiente" not in values:
        print("Coluna 'Nome do Ambiente' não encontrada")
        return
      
      ambientes_index = values.index("Nome do Ambiente")
      
      letra_index = BuscarAmbientes.numero_para_letra_coluna(self, ambientes_index + 1)
      
      valores_Coluna = (
        service.spreadsheets()
        .values()
        .get(spreadsheetId=SPREADSHEET_ID, range=f"{self.SHEET_NAME}!{letra_index}:{letra_index}")
        .execute()
      )
      return valores_Coluna.get("values", [[]])[1:]
      
      # vals = [x[0] for x in values[ambientes_index] if x and x[0].strip()]

    except HttpError as err:
      print(err)
      
      
  def numero_para_letra_coluna(self, numero):
    """Converte um índice numérico em uma letra de coluna estilo Excel."""
    letra = ""
    while numero > 0:
        numero -= 1
        letra = chr(numero % 26 + 65) + letra
        numero //= 26
    return letra