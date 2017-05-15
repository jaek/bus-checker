#!/usr/bin/python
from time import strftime, localtime
import requests
import json

# variables for headers
api_key = 'apikey wpdt9YYzWmdZjmjiFVuILrvxYkBT6Jwsyg67'
auth_url = 'https://api.transport.nsw.gov.au/v1/gtfs/realtime/buses'

# variables for GET request
url = "https://api.transport.nsw.gov.au/v1/tp/departure_mon?"
outputFormat = "rapidJSON"
coordOutputFormat = "EPSG%3A4326"
mode = "direct"
type_dm = "stop"
name_dm = "203812"
depArrMacro = "dep"
itdDate = strftime("%Y%m%d", localtime()) #date YYYYMMDD
itdTime = strftime("%H%M", localtime()) #time in 24hr

# Set the headers for request:
headers = {"Authorization": api_key, 'Accept': 'application/json'}

stopData = requests.get('{0}outputFormat={1}&coordOutputFormat={2}&mode={3}&type_dm={4}&name_dm={5}&depArrMacro={6}&itdDate={7}&itdTime={8}&TfNSWDM=true&version=10.2.1.15'.format(
    url, outputFormat, coordOutputFormat, mode, type_dm, name_dm, depArrMacro, itdDate, itdTime), headers=headers)

output = json.loads(stopData.content)
stopEvents = output['stopEvents']


for event in stopEvents:
    bus = event.get("transportation")
    bus = bus.get("disassembledName")
    print event.get("departureTimePlanned"), bus

