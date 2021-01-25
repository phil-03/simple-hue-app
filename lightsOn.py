#Turns Philip's Hue Lights 


from flask import json
from flask import Response
#from flask_cors import CORS
from flask_api import FlaskAPI, status, exceptions
from flask import request, url_for
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

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

#def lights_on():
for i in range(1, 4) :
    r = requests.put(URL + 'lights/{}/state'.format(i) ,verify=False, data=toggle1,headers=headers)
 #   return {'lights' : 'Currently On'}


#if __name__ == '__main__':
 #  app.run(debug=True, host='0.0.0.0', port=5000)
