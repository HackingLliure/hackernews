import gspread as gs
from oauth2client.service_account import ServiceAccountCredentials as sac
import pandas as pd
import json

creds_path = 'creds.json'
sheet_name = 'hackernews'

class api:
    def __init__(self, creds_path, sheet_name):
        self.creds_path = creds_path
        self.sheet_name = sheet_name
        self.scope = ['https://spreadsheets.google.com/feeds', 
                'https://www.googleapis.com/auth/drive']

    def auth(self):
        credentials = sac.from_json_keyfile_name(self.creds_path, self.scope)
        return gs.authorize(credentials)

    def open(self):
        gc = self.auth()
        return gc.open(self.sheet_name).sheet1

    def get_pd(self):
        sheet = self.open()
        data = sheet.get_all_values()

        return pd.DataFrame(data, columns = ['id', 'content'])

    def get(self, get_id):
        sheet = self.open()       
        position = sheet.find(str(get_id))
        
        try:
            data = sheet.cell(position.row, position.col + 1).value
            data = data.replace('\'', "\"") 
            print(data)
            return json.loads(data)
        except gs.exceptions.CellNotFound:
            return json.loads({ 'Error': 'Id ' + str(get_id) + ' not found.' })

    def post(self, data):
        sheet = self.open()
        
        sheet.append_row([data["id"], str(data).replace("\'", "\"")])

        return True

def test():
    test_id = 69
    
    sess = api(creds_path, sheet_name)

    df = sess.get_pd()
    print(df["id"])

    data = sess.get(test_id)
    print(data['id'], data['url'])

    test_json = { "id": 69, "url": "hackinglliure.com" }

    print(sess.post(test_json))

if __name__ == '__main__':
    test()
