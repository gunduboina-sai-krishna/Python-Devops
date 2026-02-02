# Check service status if running - exit code will be 0  
# If not active → return exit code will be 1 then restart 
# if restart not working exit code will be 2 
# Log action in monitor.log

import subprocess
import logging

service = "nginx"

logging.basicConfig(
    filename="monitor.log",
    level = logging.INFO,
    format="%(acstime)s - %(levelname)s - %(message)s"
)

def check_service():
    result = subprocess.run(
        ["systemctl", "is-active", "--quite", service]
    )
    return result.returncode

def restart_service():
    subprocess.run(
        ["systemctl", "restart", service]
    )

status = check_service()

if status == 0:
    logging.info(f"{service} is running fine")
    print("service is healthy")
    exit(0)

elif status == 1:
    logging.info(f"{service} is not running, going to rtestart")
    restart_service()

    status_after_restart = check_service()

    if status_after_restart == 0:
        logging.info(f"{service} is restarted successfully")
        print("restart successful")
        exit(1)

    elif status_after_restart == 1:
        logging.info(f"{service} is still down, manual intervention needed...")
        print("restart failed")  
        exit(2)

else:
    logging.error("unexpected error code occured")
    exit(2)          


