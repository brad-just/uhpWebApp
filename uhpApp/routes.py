from flask import render_template, url_for, redirect, request, session
from uhpApp.GoogleScripts import execute_script
import json
from uhpApp import app

@app.route("/", methods=["Get","Post"])
@app.route("/home", methods=["Get","Post"])
def home():
    events = json.loads(execute_script('mainCal')['response']['result'])
    params = ['1fhYZyb5sCBdjhHmrogAbCRySSa6GGv_OJ9LySangaj4', 'Updates'] #sheet id, sheet name
    updates = json.loads(execute_script('mainGetSheet', params=params)['response']['result'])
    return(render_template("home.html", Events=events, Updates=updates))

@app.route("/status", methods=["Get","Post"])
def status():
    if('user' in session):
        status = json.loads(execute_script('mainUserStatus', params=[session['user']])['response']['result'])
        if(status):
            if(status['sj_status']=='COMPLETE' and status['uhp_status']=='COMPLETE'):
                combined_status = 'COMPLETE'
            else:
                combined_status = 'INCOMPLETE'
            return(render_template("status.html", status=combined_status, uhp_status=status['uhp_status'], uhp_event=status['uhp_event'],
                                                  uhp_date=status['uhp_date'], sj_status=status['sj_status'], sj_event=status['sj_event'],
                                                  sj_date=status['sj_date'], member=True))
    return(render_template("status.html", status="", uhp_status="", uhp_event="",
                                          uhp_date="", sj_status="", sj_event="",
                                          sj_date="", member=False))


@app.route("/requirements", methods=["Get","Post"])
def requirements():
    return(render_template("requirements.html"))

@app.route("/FAQ", methods=["Get","Post"])
def FAQ():
    return(render_template("FAQ.html"))

@app.route("/api/RSVP", methods=["Post"])
def rsvp():
    if('user' in session):
        if('title' in request.json):
            execute_script('mainRSVP', params=[session['user'], request.json['title']])
            return(json.dumps('Successful RSVP'))
        else:
            return(json.dumps("Invalid Request"))
    else:
        return(json.dumps('Not Signed In'))

@app.route("/api/event-sign-in", methods=["Post"])
def event_sign_in():
    if('user' in session):
        if('title' in request.json and 'requirement' in request.json and 'longitude' in request.json
            and 'latitude' in request.json and 'locationCheck' in request.json):
            execute_script('mainSignIn', params=[session['user'], request.json['title'],
                                                 request.json['requirement'], request.json['longitude'],
                                                 request.json['latitude'], request.json['locationCheck']])
            execute_script('mainTracker', params=[session['user'], request.json['requirement'], request.json['title']])
            return(json.dumps('Successful Sign In'))
        else:
            return(json.dumps('Invalid post parameters'))
    else:
        return(json.dumps("Not Signed In"))

@app.route('/api/sign-in', methods=["Post"])
def sign_user_in():
    if('user' in request.json):
        session['user'] = request.json['user']
        return(json.dumps(True))
    return(json.dumps(False))

@app.route('/api/sign-out', methods=["Post"])
def sign_user_out():
    if('user' in request.json):
        session.pop('user')
        return(json.dumps(True))
    return(json.dumps(False))
