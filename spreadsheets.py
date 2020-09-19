import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)

sheet = client.open('Patient_database').sheet1


def addPatient(idnum,pname,pstatus):
    row = [idnum,pname,pstatus]
    sheet.append_row(row)


def showNameStatus():
    name = sheet.col_values(2)
    status = sheet.col_values(3)
    return name,status

def idNumber():
    count = len(sheet.col_values(1))
    return count
print(idNumber())
