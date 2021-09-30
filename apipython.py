#!/usr/bin/python3
#
import requests
import sys

tower_url='https://192.168.33.40/api/v2/job_templates/?name__contains={}'.format(sys.argv[1])
print (tower_url)

if sys.argv[1] == 'all':
   tower_url='https://192.168.33.40/api/v2/job_templates/'


response = requests.get(tower_url, verify=False, headers={"Accept":"Application/json", "Authorization":"Bearer FFsnDGoskDHA3clUVERONbOEWXvJk6"})

responseoutput = response.json()

print ("Template name\n")
for i in range(len(response.json()['results'])):
  print (responseoutput['results'][i]['name'])


