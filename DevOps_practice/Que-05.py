# How to trigger an alert from a Python script when disk space crosses a threshold?

import shutil
import smtplib
from email.mime.text import MIMEText

# Config
THRESHOLD = 80  # %
DISK_PATH = "/"
EMAIL_FROM = "alert@example.com"
EMAIL_TO = "admin@example.com"
SMTP_SERVER = "smtp.example.com"

def send_email_alert(usage_percent):
    msg = MIMEText(f"⚠️ Disk usage is at {usage_percent}%, please check {DISK_PATH}")
    msg['Subject'] = f"Disk Space Alert: {usage_percent}%"
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO

    with smtplib.SMTP(SMTP_SERVER) as server:
        server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())

def check_disk_space():
    total, used, free = shutil.disk_usage(DISK_PATH)
    percent_used = (used / total) * 100
    print(f"Disk usage: {percent_used:.2f}%")

    if percent_used > THRESHOLD:
        send_email_alert(round(percent_used, 2))

if __name__ == "__main__":
    check_disk_space()

# Slack - webhook

import shutil
import requests

SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/XXXX/XXXX/XXXX"
THRESHOLD = 80
DISK_PATH = "/"

def send_slack_alert(usage_percent):
    payload = {"text": f"🚨 Disk usage is at {usage_percent}% on {DISK_PATH}"}
    requests.post(SLACK_WEBHOOK_URL, json=payload)

def check_disk():
    total, used, free = shutil.disk_usage(DISK_PATH)
    percent_used = (used / total) * 100
    if percent_used > THRESHOLD:
        send_slack_alert(round(percent_used, 2))

if __name__ == "__main__":
    check_disk()


# Shutil (standard library) - General file operations (copy, move, delete, archive, disk usage). no extra installations.
# psutil (3rd party library) - System monitoring (CPU, memory, disk, network, processes, sensors, etc.).