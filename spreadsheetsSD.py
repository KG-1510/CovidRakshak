import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('credentialsSD.json', scope)
client = gspread.authorize(creds)

sheet = client.open('Social_distancing').sheet1

def sdData(st,et,mov,date):
    row = [st,et,mov,date]
    sheet.append_row(row)