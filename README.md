# pi-wap
Configure a Raspberry Pi to be a wireless access point and a very simple Flask-based web page to show status.

## Wireless Access Point Software and Congig
Software and configuration to create the WAP came from the article Setting up a *Raspberry Pi as a Wireless Access Point* found here on the [RaspberryPi.org](https://www.raspberrypi.org) site:
<https://www.raspberrypi.org/documentation/configuration/wireless/access-point.md>

Everything was setup using the defaults, including 
```
hw_mode=g
channel=7
```
In the file 
`/etc/hostapd/hostapd.conf`

## Initial Flask App
The initial flask app was written following the *Quickstart* article on the website <https://flask.palletsprojects.com> found here:
<https://flask.palletsprojects.com/en/1.1.x/quickstart/>

## NGINX based Flask server
To automatically have the Pi serve up the flask page, the article *Running Flask under NGINX on the Raspberry Pi* was followed, found here:
<https://www.raspberrypi-spy.co.uk/2018/12/running-flask-under-nginx-raspberry-pi/>

### Changes
Created a directory structure
```
/home/pi/flask/
/home/pi/flask/flask_app/    # Has the python that flask runs
/home/pi/flask/flask_server/ # Has the file flask_app_proxy
```

Instead of using the app name `flasktest` am using `flask_app`.

Thus the file `flasktest_proxy` becomes `flask_app_proxy`

And instead of using the symbolic link
`/etc/nginx/sites-available/flasktest_proxy -> /etc/nginx/sites-enabled`
am using 
`/etc/nginx/sites-enabled/flask_app_proxy -> /home/pi/flask/flask_server/flask_app_proxy`

## Flask app setup

