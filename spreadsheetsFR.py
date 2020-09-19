import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('credentialsFR.json', scope)
client = gspread.authorize(creds)

FRsheet = client.open('Face_recognition').sheet1

def detectPatient(idnum,pname,time,date,status):
    row = [idnum,pname,time,date,status]
    FRsheet.append_row(row)