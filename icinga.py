#!/usr/bin/env python3

import http.client
from base64 import b64encode
import json
import sys

conn = http.client.HTTPSConnection(sys.argv[2])

credentials = bytearray(sys.argv[1], encoding='utf8')

userAndPass = b64encode(credentials).decode("ascii")
headers = { 'Authorization' : 'Basic %s' %  userAndPass }
conn.request("GET", "/cgi-bin/icinga/tac.cgi?jsonoutput", headers=headers)
res = conn.getresponse()

data = json.loads(res.read())

data['tac']['tac_overview']['title'] = sys.argv[3]

if int(data['tac']['tac_overview']['hosts_down']) > 0 or \
   int(data['tac']['tac_overview']['hosts_down_scheduled']) > 0 or \
   int(data['tac']['tac_overview']['hosts_down_acknowledged']) > 0:
   data['tac']['tac_overview']['hosts_down_color'] = 'red'
else:
   data['tac']['tac_overview']['hosts_down_color'] = 'default'

if int(data['tac']['tac_overview']['services_warning']) > 0 or \
   int(data['tac']['tac_overview']['services_warning_scheduled']) > 0 or \
   int(data['tac']['tac_overview']['services_warning_acknowledged']) > 0:
   data['tac']['tac_overview']['service_warning_color'] = 'yellow'
else:
   data['tac']['tac_overview']['service_warning_color'] = 'default'

if int(data['tac']['tac_overview']['services_critical']) > 0 or \
   int(data['tac']['tac_overview']['services_critical_scheduled']) > 0 or \
   int(data['tac']['tac_overview']['services_critical_acknowledged']) > 0:
   data['tac']['tac_overview']['service_critical_color'] = 'red'
else:
   data['tac']['tac_overview']['service_critical_color'] = 'default'

html = '''
<div id="widget">
   <div id="header">
   {title}
   </div>
   <div id="cell" class="green">
   {hosts_up} UP
   </div>
   <div id="cell" class="{hosts_down_color}">
   {hosts_down} / {hosts_down_scheduled} / {hosts_down_acknowledged} DOWN
   </div>
   <br>
   <div id="cell" class="green">
   {services_ok} OK
   </div>
   <div id="cell" class="{service_warning_color}">
   {services_warning} / {services_warning_scheduled} / {services_warning_acknowledged} WARNING
   </div>
   <div id="cell" class="{service_critical_color}">
   {services_critical} / {services_critical_scheduled} / {services_critical_acknowledged} CRITICAL
   </div>
<div>
'''.format( **data['tac']['tac_overview'])
print(html)