# parse the logs, print distinct logs
# 1. store all errors in a list
error = []
with open('/Users/gunduboina.saikrishna/app.log') as f:
    for line in f:
        if "ERROR" in line:
            error.append(line.strip())
#print(error)      

#2. If you want count of each repeated error (real-world use)

error = {}

with open('/Users/gunduboina.saikrishna/app.log') as f:
    for line in f:
        if "ERROR" in line:
            msg = line.strip()
            error[msg] = error.get(msg, 0) + 1
#print(error)      

# count Errors

error_count = 0

with open("/Users/gunduboina.saikrishna/app.log") as f:
    for line in f:
        if "ERROR" in line:
            error_count += 1
print(f"Total errors count: {error_count}")        


## Print unique errors

unique_errors = set()

with open("/Users/gunduboina.saikrishna/app.log") as f:
    for line in f:
        if "ERROR" in line:
            error_msg = line.split("ERROR") [-1].strip()
            unique_errors.add(error_msg)
print("distinct_errors: \n")  
for err in unique_errors:
    print(err)          


#3. Write Python to check CPU and memory usage.

import psutil

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent

print(f"CPU's usage: {cpu}%")
print(f"Memory usage: {memory}%")

if cpu > 1:
    print("High cpu alert")



#4. API Health Check Script

import requests

url = "https://google.com/health"
res = requests.get(url)

if res.status_code == 200:
    print("API health is good")
else:
    print("API is Down")    


#5. Read YAML Config (Infra Automation)

#server:
  #host: localhost
  #port: 8080

import yaml

with open("server.yaml") as f:
    config = yaml.safe_load(f)
print(config["server"]["host"])    


#6. Retry Logic (Important for APIs)

import time
import requests

for i in range(3):
    try:
        url = "https://google.com/health"
        res = requests.get(url)
        print("success")
        break
    except:
        print("Retrying")
        time.sleep(2)

#7. Check Disk Usage (Linux Automation)

import shutil

total, used, free = shutil.disk_usage("/")
used_disk_percent = (used / total) * 100

if used_disk_percent > 20:
    print("high disk pressure")

