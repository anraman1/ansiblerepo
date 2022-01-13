#!/usr/bin/env python3

import datetime
import json

from ansible.module_utils.basic import AnsibleModule
#DOCUMENTATION = r'''
#---
#module: timetest
#short_descrition: Display time
#version: 1.10
#description: This is a testing moudle to print time 
#...
#EXAMPLES =  r'''
#---
#- name: display time
#  timetest: 
#...

def now():
  date = str(datetime.datetime.now())
  return date 

def utc():
  date = str(datetime.datetime.utcnow())
  return date

def main():
  #date = str(datetime.datetime.now())
  #print(json.dumps( { "time" : date } ))
  #return (json.dumps( { "time" : date } ))
  fields = { "utc": { "required": False, "type": "bool", "default": False} }
  result = {" changed": False, "date": "" }
  module = AnsibleModule(argument_spec=fields)
  if module.params["utc"]:
     result["date"] = utc()
  else:
   result["date"] = now()
  module.exit_json(**result)
if __name__ == '__main__':
   print(main(),exit())
