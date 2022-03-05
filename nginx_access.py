
import os
import sys
import json
from ansible.module_utils.basic import AnsibleModule
import subprocess




def check_logs_502()
    proc =  p = subprocess.Popen("cat /var/log/nginx/access.log|awk '{print $9}'|grep 502", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    print p.split("\n")
def check_logs_200()
    proc =  p = subprocess.Popen("cat /var/log/nginx/access.log|awk '{print $9}'|grep 200", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    print p.split("\n")
def check_logs_403()
    proc =  p = subprocess.Popen("cat /var/log/nginx/access.log|awk '{print $9}'|grep 403", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    print p.split("\n")

def main():
    chef_log_502()

if __name__ == __main__:
    main()




       


