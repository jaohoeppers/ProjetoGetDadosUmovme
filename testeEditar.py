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
SHEET_NAME = "2025"
SHEET_COLLUM = "G"

# RANGE_NAME = "2025!G"
class teste:
  
  def __init__(self):
    self.service = None

  def main(self):
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
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

    try:
      self.service = build("sheets", "v4", credentials=creds)
      
    except HttpError as err:
      print(err)
      
      

  def update_cell(self, spreadsheet_id, sheet_name, cell, new_value):
      """
      Atualiza o valor de uma célula em uma planilha do Google Sheets.

      Args:
          service: Objeto de serviço da API do Google Sheets.
          spreadsheet_id: ID da planilha.
          sheet_name: Nome da aba da planilha.
          cell: Referência da célula (ex: "G2").
          new_value: Novo valor para a célula.
      """
      range_ = f"{sheet_name}!{cell}"
      body = {
          "range": range_,
          "values": [[new_value]]
      }
      result = self.service.spreadsheets().values().update(
          spreadsheetId=spreadsheet_id,
          range=range_,
          valueInputOption="RAW",
          body=body
      ).execute()
      print(f"Célula {cell} atualizada com sucesso para: {new_value}")

if __name__ == "__main__":
  teste = teste()
  teste.main()
  teste.update_cell(SPREADSHEET_ID, SHEET_NAME, "O96", "TESTEEE")