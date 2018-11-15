import gspread as gs
from oauth2client.service_account import ServiceAccountCredentials as sac
import pandas as pd

creds_path = 'creds.json'
sheet_name = 'hackernews'

def auth(creds_path):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = sac.from_json_keyfile_name(creds_path, scope)
    return gs.authorize(credentials)

def get_sheet():
    gc = auth(creds_path)

    sheet = gc.open(sheet_name).sheet1
    data = sheet.get_all_values()

    return pd.DataFrame(data, columns = ['id', 'content'])

def get_by_id(get_id):
    gc = auth(creds_path)

    sheet = gc.open(sheet_name).sheet1
    position = sheet.find(get_id)
    
    return sheet.cell(position.row, position.col + 1).value

def test():
    data = get_sheet()
    print(data)

    print(get_by_id('test'))

if __name__ == '__main__':
    test()
