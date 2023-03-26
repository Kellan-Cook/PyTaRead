import subprocess
import json
import string
from marshmallow import Schema, fields, post_load
import os
import re


#By Kellan Cook

#Schema for encoding
class ServiceListSchema(Schema):
    image = fields.Str()
    pid = fields.Int()
    sessionName = fields.Str()
    sessionNum = fields.Int()
    memUsage = fields.Str()

#Object for each service
class ServiceList():
    def __init__(self, image, pid, sessionName, sessionNum, memUsage):
        self.image = image
        self.pid = pid
        self.sessionName = sessionName
        self.sessionNum = sessionNum
        self.memUsage = memUsage




def checkServices():




    
    curentTasks = subprocess.check_output(['tasklist']).splitlines()
    output = []
    systemservices = []
    
    for tasks in curentTasks:
        stask = tasks.decode(encoding= "utf-8", errors= "ignore")
        m = re.match("(.+?) +(\d+) (.+?) +(\d+) +(\d+.* K).*",stask)
        if m is not None:
            output.append({"image":m.group(1),
                            "pid":m.group(2),
                            "sessionName":m.group(3),
                            "sessionNum":m.group(4),
                            "memUsage":m.group(5)
                            })
            systemservices.append(ServiceList(m.group(1), m.group(2), m.group(3), m.group(4), m.group(5)))

            systemservices
        
            

    print("===================================== ALL SERVICES DETECTED =====================================")
    for line in output:
        print(line)
    print("=================================== END OF SERVICES DETECTED ====================================\n\n")
    print("would you like to save any of the services to the white list? if yes ENTER: the PID of the service if no ENTER: N")
    a = input()

    if(a.lower != 'n'):
        for service in systemservices:
            if(str(service.pid) == str(a)):
                


print("press [C] to run check \n[B] to edit blacklist \n[W] to edit Whitelist \n[N] to edit known service list")
a = input()



if(a.lower() == 'c'):
    checkServices()

