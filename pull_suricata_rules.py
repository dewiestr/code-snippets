#!/usr/bin/python
import requests
import urlparse
import os
import io

""" Script that gets the last $days number of suricata rules from MISP.
"""

remote = "" #MISP URL
key = "" #MISP KEY
days = 400
Filename = "misp_last_%d_days.rules" %days

headers= {"Authorization":key}

url_suricata = urlparse.urljoin(remote,os.path.join("/events/nids/suricata/download/","false","false","false","false","false",str(days)+"d"))
r = requests.get(url_suricata,headers=headers, stream=True,verify=False)

with io.open(Filename,"w", encoding='utf-8') as file:
	file.write(r.text)
