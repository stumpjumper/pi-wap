#!/usr/bin/env python3

import subprocess
import time
from flask import Flask
from list_wifi_clients import *

app = Flask(__name__)

def getUptime():
  uptimeRun = subprocess.run(['uptime'],check=True,stdout=subprocess.PIPE)
  uptimeString = bytes.decode(uptimeRun.stdout)
  return uptimeString

def getPrettyUptime():
  uptime = getUptime()
  uptime = uptime.split("up")
  uptime = uptime[1].strip()
  uptime = "Up time: " + uptime
  uptime = uptime.replace("load average","Load average")
  return uptime

def getDateTime():
  return time.asctime()

def getCPUTemp(fahrenheit=False):
  tempFile = open('/sys/class/thermal/thermal_zone0/temp','r')
  for line in tempFile:
    temp = line.strip()
  tempFile.close()

  temp = int(temp)/1000
  if fahrenheit:
    temp = temp*1.8 + 32.0

  return temp

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

  uptime   = getPrettyUptime()
  dateTime = getDateTime()
  fahrenheit = True
  temp     = getCPUTemp(fahrenheit=fahrenheit)

  tempType = "C"
  maxTemp  = "82°C"
  if fahrenheit:
    tempType = "F"
    maxTemp  = "180°F"

  myListWiFiClients = ListWiFiClients()

  #print ("Connected Devices:")
  conDevicesString = myListWiFiClients.getConDevicesTableString()
  #conDevicesString = conDevicesString.replace('\n', '<br>\n')

  #print ("DHCP Leases:")
  dhcpLeasesString = myListWiFiClients.getDHCPLeasesTableString()
  #dhcpLeasesString = dhcpLeasesString.replace('\n', '<br>\n')

  msg="""\
<p>%s</p>
<p>%s</p>
<p>CPU Temp: %.1f°%s (< %s is good)</p>
Connected Devices
<pre>
%s
</pre>
<br>DHCP Leases
<pre>
%s
</pre>
  """ % (dateTime, uptime, temp, tempType, maxTemp, conDevicesString,
         dhcpLeasesString)

  return msg

if __name__ == "__main__":
  arg1 = ""
  if len(sys.argv) > 1:
    arg1 = sys.argv[1].lower()
  if "-h" in arg1:
    print("Pass -cl flag to dump output to command line")
  elif "-cl" in arg1:
    print (dhpc_status())
  else:
    app.run(host='0.0.0.0',debug=True)
