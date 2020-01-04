This directory contains copies of the system files that were modified to create the wireless access point.  This was done followng the directions found here:
https://www.raspberrypi.org/documentation/configuration/wireless/access-point.md
A pdf of this file is on my Google Drive

The files in this directory were copied using the commands below.

<pre>
# Wireless access point:
cp /etc/dhcpcd.conf .
cp /etc/dnsmasq.conf .
cp /etc/hostapd/hostapd.conf . # NOTE: Edit to take out passwords
cp /etc/default/hostapd .
cp /etc/sysctl.conf .
cp /etc/iptables.ipv4.nat .

# Setup for outside wirless networks:
cp /etc/wpa_supplicant/wpa_supplicant.conf . # NOTE: Edit to take out passwords
</pre>
