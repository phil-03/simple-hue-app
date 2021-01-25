#Setup for Philips Hue
#The hue system is built around the idea of everything in your system having a unique URL served by the bridge. 
#General tasks
#-Lights turn on when MAC is detected
#-Can adjust lights from anywhere
#-Can adjusts who can control them

from flask import json
from flask import Response
#from flask_cors import CORS
from flask_api import FlaskAPI, status, exceptions
from flask import request, url_for
import requests
#Tokens - constants used to parse tress or JSON
Dict = {'BRIDGE_IP':'192.168.1.13', 'API_KEY':'e5XZwtux-QKg5rsc575f8ZTpHR5-O8ZmWCe42ywl','SAT':'254','BRI':'254'}

bridge_ip = Dict['BRIDGE_IP']
api_key = Dict['API_KEY']

#Each light has its own URL. 
URL = 'https://' + bridge_ip + '/api/' + api_key + '/'
app = FlaskAPI(__name__)


#SAMPLE HUE ATTRIBUTES - {"on":true, "sat":254, "bri":254,"hue":10000}
#Basic hue settings for from Phillips
   
toggle1 = " {\"on\":true }"
toggle2 = " {\"on\":false }"
headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache"
} 

@app.route('/')
def index():
    return 'Hi Phil'

#Should give a JSON response with all the lights on my network plus their names
@app.route('/lights')
def get_lights():
     r = request
     return requests.get(URL + 'lights', verify=False).json()

#Use a put to make a request towards hue attributes
@app.route('/lightsoff')
def lights_off():
    for i in range(1, 4) :
       r = request
       r = requests.put(URL + 'lights/{}/state'.format(i) ,verify=False, headers=headers, data=toggle1)
    return {'lights' : 'Currently Off'}

@app.route('/lightson')
def lights_on():
    for i in range(1, 4) :
       r = request
       r = requests.put(URL + 'lights/{}/state'.format(i) ,verify=False, headers=headers, data=toggle2)
    return {'lights' : 'Currently On'}

#Make sure once MAC address is detected that all this is triggered.



if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=5000)


#When we run application as script, the Flask's inbuilt server starts on port 5000 due to APP.run
#Here we instruct APP(which we defined already as Flask's instance), to run the server at 0.0.0.0(localhost/127.0.0.1) which is Flask's inbuilt WSGI server

