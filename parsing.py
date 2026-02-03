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


#1. Count Errors by Type

counts = {"ERROR": 0, "WARNING": 0, "INFO": 0}

with open("/Users/gunduboina.saikrishna/app.log") as f:
    for line in f:
        for level in counts:
            if level in line:
                counts[level] += 1
print(counts)                


#Find Top N Frequent Errors

from collections import Counter

errors = []

with open("/Users/gunduboina.saikrishna/app.log") as f:
    for line in f:
        if "ERROR" in line:
            msg = line.split("ERROR")[-1].strip()
            errors.append(msg)

top = Counter(errors).most_common(3)
print(top)


#Detect Repeated Failures per IP

import re
from collections import Counter

THRESHOLD = 5
ips = []
pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+)')

with open("/Users/gunduboina.saikrishna/app.log") as f:
    for line in f:
        if "failed" in line:
            match = pattern.search(line)
            if match:
                ips.append(match.group())

counts = Counter(ips) 

for ip, count in counts.items():
    if count > THRESHOLD:
        print(f"🚨 ALERT: Possible attack from {ip} ({count} failures)")



# Log File Size Monitor - alert if file size is more than 1GB

import os

size = os.path.getsize("/Users/gunduboina.saikrishna/app.log") / (1024**3)
if size > 1:
    print("log size is more than 1GB")

