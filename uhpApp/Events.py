#
# Description: Events is a class that stores event information for upcoming events. Data stored are
# (1) Event Name (2) Event Date (3) Event Location (4) Event Time (5) Event Requirement
# Date: 9/7/19
# Coder: Brad Just
#
from uhpApp.GoogleScripts import execute_script
from requests import get
import json

class Events(object):
    def __init__(self):
        self.events = None
        self.function_name = 'mainCal'
    def setEvents(self):
        '''A Method that sets updates from Google Apps Script'''
        data = execute_script(self.function_name)
        self.events = json.loads(data['response']['result'])
