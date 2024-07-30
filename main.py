import os
import pickle
import subprocess
import time
import schedule
import nbformat
from nbconvert import HTMLExporter
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from getpass import getpass

def confirm_credentials():
    # Check for existing credentials
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
            print(f"Current credentials: {creds}")
            use_existing = input("Do you want to use these credentials? (yes/no): ").strip().lower()
            if use_existing == 'yes':
                return creds
    # If no existing credentials or user wants to use new ones
    username = input("Enter your Gmail username: ")
    password = getpass("Enter your Gmail password: ")
    creds = {"username": username, "password": password}
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)
    return creds

def send_email(subject, body, to_email, creds):
    from_email = creds["username"]
    password = creds["password"]
    
    # Create email message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    
    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))
    
    # Send email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

def run_notebook():
    subprocess.run(["jupyter", "nbconvert", "--to", "notebook", "--execute", "news_processor.ipynb"])

def read_summary():
    with open('news_summary.md', 'r') as file:
        return file.read()

def main():
    creds = confirm_credentials()
    
    schedule_option = input("Do you want to run this script every 3 days? (yes/no): ").strip().lower()
    
    def job():
        run_notebook()
        summary = read_summary()
        send_email("Newsletter Summary", summary, creds["username"], creds)
    
    if schedule_option == 'yes':
        schedule.every(3).days.do(job)
        print("Scheduled to run every 3 days. Press Ctrl+C to exit.")
        while True:
            schedule.run_pending()
            time.sleep(1)
    else:
        job()

if __name__ == "__main__":
    main()
