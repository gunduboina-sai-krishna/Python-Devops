logs = [
    "10.0.0.1 - - 200 OK",
    "10.0.0.2 - - 500 Internal Server Error",
    "10.0.0.3 - - 404 Not Found",
    "10.0.0.4 - - 500 Internal Server Error",
]
ans = sum('500' in line for line in logs)
print(ans)


import re
email = "Contact: test@gmail.com, admin@example.com, hr@gmail.com"
domain = list(set(re.findall(r'@([\w\.-]+)', email)))
print(domain)

list1 = [12.3456, 78.9012, 33.3333]
normalized = [round(num, 2) for num in list1]
print(normalized)

mem = {"node1": 60, "node2": 85, "node3": 40}
max_node = max(mem, key=mem.get)
print(max_node, mem[max_node])

import os
import glob

def large_files():
    
    dir = "/var/log"
    threshold = 500 * 1024 * 1024

    for file_path in glob.glob(dir):
        if os.path.isfile(file_path):
            size_bytes = os.path.getsize(file_path)
            size_mb = size_bytes / ( 1024 * 1024 )
            if size_mb >= threshold:
                print(f"filename : {file_path} is large file with ({size_mb:.2f}MB)")  


    