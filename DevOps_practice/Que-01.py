# Check All Files in a Directory for Size > 100MB

import os
import glob

directories = ["/var/log/*", "/tmp/*"]
threshold = 100 * 1024 * 1024  # 100MB in bytes

for i in directories:
    for file_path in glob.glob(i):
        if os.path.isfile(file_path):
            try:
                size_bytes = os.path.getsize(file_path)
                if size_bytes >= threshold:
                    size_mb = size_bytes / (1024 * 1024)
                    print(f"File over 100MB: {file_path} ({size_mb:.2f} MB)")
            except Exception as e:
                print(f"Error reading {file_path}: {e}")



#Delete or archive files older than X days.
 
import os
import time
import glob


folder = ['/var/log/*']
days = 7
now = time.time()

cutoff = now - (days*86400)

for file in os.listdir(folder):
    path = os.path.join(folder, file)

    if os.path.isfile(folder):
        if os.stat(path).st_mtime < cutoff:
            print(f"delete the {path}")
            os.remove(path)    
        
# To Archive with glob - first compress then move to archive

import os
import time
import glob
import shutil
import gzip

SOURCE = "/var/log"
ARCHIVE = "/var/backup/archive"
days = 30
cutoff = time.time() - (days * 86400)

os.makedirs(ARCHIVE, exist_ok=True)

for path in glob.glob(f"{SOURCE}/*.log"):
    if os.path.isfile(path) and os.stat(path).st_mtime < cutoff:

        filename = os.path.basename(path)
        compres_file = path + ".gz"

        with open(path, 'rb') as f_in, gzip.open(compres_file, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

        shutil.move(compres_file, os.path.join(ARCHIVE, filename + ".gz"))
        os.remove(path)

        print(f"Archived: {filename}")    







# * glob module:
# The glob module in Python is used to search for files and directories whose names match a specified pattern (with wildcards like *, ?, [], etc.).

# It returns a list of matching file paths.

# ✅ pattern:
# In your code, pattern comes from the list:
# directories = ["/var/log/*", "/tmp/*"]
# So, for example, pattern = "/var/log/*"

# ✅ glob.glob(pattern):
# This expands the wildcard pattern like a shell would.

# Example:

# glob.glob("/var/log/*")

# might return:

# [
#   '/var/log/syslog',
#   '/var/log/auth.log',
#   '/var/log/dpkg.log',
#   '/var/log/private',
#   ...
# ]

#In {size_mb:.2f}:

# f → format the number as a floating-point (decimal) value

# .2 → keep 2 digits after the decimal point
