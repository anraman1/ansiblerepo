#!/usr/bin/env python3

import os
import sys
import json
from ansible.module_utils.basic import AnsibleModule
import subprocess




def check_logs_502():
    proc =  p = subprocess.Popen("cat /var/log/nginx/access.log|awk '{print $9}'|grep 502", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    return(p.split("\n"))
def check_logs_200():
    proc =  p = subprocess.Popen("cat /var/log/nginx/access.log|awk '{print $9}'|grep 200", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    return(p.split("\n"))
def check_logs_403():
    proc =  p = subprocess.Popen("cat /var/log/nginx/access.log|awk '{print $9}'|grep 403", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    return (p.split("\n"))
def check_logs_all():
    proc =  p = subprocess.Popen("cat /var/log/nginx/access.log|awk '{print $9}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    return(p.split("\n"))

def main():
    fields = { "statuscode": { "required": False, "type": "int", "default": ""} }
    result = {"changed": False, "statusout": "" }
    module = AnsibleModule(argument_spec=fields)
    if module.params["statuscode"]:
        if module.params["statuscode"] == 200:
          result["statusout"] = check_logs_200()
        elif module.params["statuscode"] == 502:
          result["statusout"] = check_logs_502()
        elif module.params["statuscode"] == 403:
          result["statusout"] = check_logs_403()
        elif module.params["statuscode"] == "all":
          result["statusout"] = check_logs_all()
          return result 
    else:
       result["statusout"] = check_logs_all()
       #module.exit_json(**result)
       
    module.exit_json(**result)
    
    

if __name__ == '__main__':
    main()

