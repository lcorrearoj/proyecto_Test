#!/usr/bin/python3

import json
import requests
import urllib3
# import pdb; pdb.set_trace()

with open("satori-endpoints.json", "r") as archivo:
    endpoints = json.load(archivo)

for url_dict in endpoints["data"]:
    print(url_dict["path"])
    for method in url_dict["methods"]:
        url = 'https://192.168.223.45' + url_dict["path"]
        if (method == "GET"):        
            response = requests.get( url , verify=False)
            print ("URL: %s STATUS %s " % (url, response.status_code))
            urllib3.disable_warnings()

