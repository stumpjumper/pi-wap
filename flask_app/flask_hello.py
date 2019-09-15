#!/usr/bin/env python

from flask import Flask
from list_wifi_clients import *

app = Flask(__name__)

@app.route('/hello-world')
def hello_world():
  msg="""
  Hello world!<br>
  <br>
  This is a line of text<br>
  And another line of text<br>
  And one more!<br>
"""
  return msg


@app.route('/')
def dhpc_status():

  myListWiFiClients = ListWiFiClients()

  #print ("Connected Devices:")
  conDevicesString = myListWiFiClients.getConDevicesTableString()
  #conDevicesString = conDevicesString.replace('\n', '<br>\n')

  #print ("DHCP Leases:")
  dhcpLeasesString = myListWiFiClients.getDHCPLeasesTableString()
  #dhcpLeasesString = dhcpLeasesString.replace('\n', '<br>\n')

  msg ="Connected Devices\n"
  msg+="<pre>\n"
  msg+=conDevicesString
  msg+="</pre>\n"
  msg+="<br>DHCP Leases\n"
  msg+="<pre>\n"
  msg+=dhcpLeasesString
  msg+="</pre>\n"
  return msg

