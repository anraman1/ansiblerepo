#!/usr/bin/python3
#
import requests
response = requests.get('https://192.168.33.40/api/v2/job_templates/', verify=False, headers={"Accept":"Application/json", "Authorization":"Bearer FFsnDGoskDHA3clUVERONbOEWXvJk6"})

responseoutput = response.json()

print ("Template name\n")
for i in range(len(response.json()['results'])):
  print (responseoutput['results'][i]['name'])


