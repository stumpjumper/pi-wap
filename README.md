# pi-wap
Configure a Raspberry Pi to be a wireless access point and a very simple Flask-based web page to show status.

A general overview on how to use and configure the access point can be found in my Google Drive in the README file on my Google Drive in the folder `GDrive Manuals/Computers/Raspberry Pi/Wireless Access Point and Flask-Based Status Page`

## Wireless Access Point Software and Config
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

#### NOTES
1) `/etc/nginx/sites-enabled/flask_app_proxy` is not directly linked to `pi-wap/flask/flask_server/flask_app_proxy` because of permissions issues.  Instead, needed files are copied to `/home/pi/flask` using the command `sudo /home/pi/flask/get_changed_files`, which copies as root via a rsync command the needed files from this repository. The command is archived as the repository file `flask/get_changed_files.see_README`
2) Even with the tricks played above for the Flask Sever, the Flask app is still `/home/pi/projects/pi-wap/flask/flask_app/flask_app.py` as set in `pi-wap/flask/flask_server/uwsgi.ini` **so the path in `uwsgi.ini` will have to be changed if the repository location is changed on the Raspberry Pi**.  This is bad because things need to be changed in two places.  It is good because changes to flask_app.py take place right away, instead of having to always execute `get_chagned_files`.

## Flask app setup
Need more content here...
