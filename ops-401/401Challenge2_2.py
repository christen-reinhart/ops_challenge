import os
import platform
import subprocess
import time
import smtplib
from email.mime.text import MIMEText

def ping_host(target_ip):
    # ... (same as before)

def send_email(subject, body):
    sender_email = "your_email@gmail.com"
    sender_password = "your_password"
    receiver_email = "admin@example.com"  # Replace with the administrator's email address

    message = MIMEText(body)
    message["Subject"] = subject
    message["From"] = sender_email 
    message["To"] = receiver_email

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email notification sent successfully.")
    except Exception as e:
        print(f"Error sending email notification: {e}")

def write_to_log(timestamp, status, target_ip, log_file):
    # ... (same as before)

def main():
    target_ip = input("Enter the target IP address: ")
    log_file = "uptime_log.txt"
    email_notification_enabled = False

    email_choice = input("Do you want to enable email notifications? (yes/no): ").lower()
    if email_choice == "yes":
        email_notification_enabled = True
        email = input("Enter your email address: ")
        password = input("Enter your email password: ")

    previous_status = None

    while True:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        status = ping_host(target_ip)

        if previous_status is not None and status != previous_status:
            subject = "Host Status Change Notification"
            body = f"Host status changed from {'Active' if previous_status else 'Inactive'} to {'Active' if status else 'Inactive'} at {timestamp}"
            send_email(subject, body)

        print(f"{timestamp} Network {'Active' if status else 'Inactive'} to {target_ip}")

        write_to_log(timestamp, status, target_ip, log_file)

        previous_status = status

        time.sleep(2)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting the uptime sensor tool.")