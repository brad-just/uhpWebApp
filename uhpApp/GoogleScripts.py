from __future__ import print_function
import pickle
import os.path
from googleapiclient import errors
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

def execute_script(function_name,
                   params=[],
                   credentials_path='/Users/bradjust/Projects/UHP-Projects/UHP-WebApp/uhpApp/credentials.json',
                   script_id='1U5EVYxC__c5V9n9DweLxz1ILy2Jk77ZYxsT3cOAGZHFzsa14BDwPZNE2',
                   SCOPES=['https://www.googleapis.com/auth/spreadsheets',
                           'https://www.googleapis.com/auth/calendar',
                           'https://www.googleapis.com/auth/forms',
                           'https://www.googleapis.com/auth/script.send_mail']):
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            creds = flow.run_local_server()
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('script', 'v1', credentials=creds)
    try:
        request = {"function": function_name, "parameters": params}
        response = service.scripts().run(body=request,scriptId=script_id).execute()
        return(response)
    except errors.HttpError as error:
        print(error.content)
