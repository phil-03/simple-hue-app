#Philip Butts
#Program scans for available addresses to locate specific mac address
#If MAC address is found it executes

import nmap
import webApp
import time
import threading
import sys, nmap, json, ipaddress, argparse
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def findMac():
   # threading.Timer(5.0, findMac).start()
    #nmap -sP -PI -PT  192.168.1.1/24
   while True:
       nm = nmap.PortScanner()
       nm.scan(hosts='192.168.1.1/24', arguments='-sP -PI -PT')
       for ip in nm.all_hosts():
           host = nm[ip]
           mac = "-"
           vendorName = "-"
           if 'mac' in host['addresses']:
               mac = host['addresses']['mac']
               if mac in host['vendor']:
                   vendorName = host['vendor'][mac]

           status = host['status']['state']
           rHost = {'ip': ip, 'mac': mac, 'vendor': vendorName, 'status': status}
        
           #Search for iphone
           if rHost['mac'] == 'F4:06:16:5B:7F:53':
               print("You have found your iphone's MAC")
               exec(open("lightsOn.py").read())
           else:
               print("Phone not present...")

       time.sleep(5)

findMac()

