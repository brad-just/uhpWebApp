#
# Description: Update is a class that stores program updates (with their authors).
# Date: 9/7/19
# Coder: Brad Just
#
from uhpApp.GoogleScripts import execute_script
from requests import post
import json

class Updates(object):
    def __init__(self):
        self.updates = None
        self.sheet_name = 'Updates'
        self.sheet_id = "1fhYZyb5sCBdjhHmrogAbCRySSa6GGv_OJ9LySangaj4"
        self.function_name = 'mainGetSheet'

    def setUpdates(self):
        '''A Method that sets updates from Google Apps Script'''
        params = [self.sheet_id, self.sheet_name]
        data = execute_script(self.function_name, params=params)
        self.updates = json.loads(data['response']['result'])
