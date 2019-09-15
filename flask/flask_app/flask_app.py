#!/usr/bin/env python

import subprocess
from flask import Flask
from list_wifi_clients import *

app = Flask(__name__)

def getUptime():
  uptimeRun = subprocess.run(['uptime'],check=True,stdout=subprocess.PIPE)
  uptimeString = bytes.decode(uptimeRun.stdout)
  return uptimeString

@app.route('/hello-world')
def hello_world():
  msg="""
  Hello world!<br>
  <br>
  This is a line of text<br>
  And another line of
  text<br>
  And one more!<br>
"""
  return msg

@app.route('/')
def dhpc_status():

  uptime = getUptime()
  uptime = "Time: " + uptime
  uptime = uptime.replace(" up",", Up time:")
  uptime = uptime.replace("load average","Load average")

  myListWiFiClients = ListWiFiClients()

  #print ("Connected Devices:")
  conDevicesString = myListWiFiClients.getConDevicesTableString()
  #conDevicesString = conDevicesString.replace('\n', '<br>\n')

  #print ("DHCP Leases:")
  dhcpLeasesString = myListWiFiClients.getDHCPLeasesTableString()
  #dhcpLeasesString = dhcpLeasesString.replace('\n', '<br>\n')

  msg ="<p>%s</p>\n" % uptime
  msg+="Connected Devices\n"
  msg+="<pre>\n"
  msg+=conDevicesString
  msg+="</pre>\n"
  msg+="<br>DHCP Leases\n"
  msg+="<pre>\n"
  msg+=dhcpLeasesString
  msg+="</pre>\n"
  return msg

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)
