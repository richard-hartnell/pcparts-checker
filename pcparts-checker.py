#!/usr/bin/python
import praw
import pdb
import re
import os
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def make_alert(part):
    return f"Hey, I found a {part} on /r/buildapcsales!"

# Your email and password
email_address = "richard@bellinghamcircusguild.com"
with open('email_password.txt', 'r') as file:
    email_password = file.read().strip()

# Email setup
def send_email(recipient_email, subject, body):
    # Create the email content
    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = recipient_email
    msg['Subject'] = subject
    
    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        # Connect to the Dreamhost SMTP server
        with smtplib.SMTP_SSL('smtp.dreamhost.com', 465) as server:
            server.login(email_address, email_password)
            # Send the email
            server.sendmail(email_address, recipient_email, msg.as_string())
            print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

# Example usage
# send_email("rfreemanh@gmail.com", "Test Subject", week_reminder)

print("Running.")

searchTerms = ("Taichi Lite",
            #    "Shadow Base",
            #    "Dark Base",
               "9900X",
               "DDR5",
               "M.2",
               "5080",
               "7950X",
               "Super Flower",
               "DDR5")
posts_found = []
subreddit = reddit.subreddit('buildapcsales')
reddit = praw.Reddit('bot1')

with open("posts_found.txt", "r") as f:
    posts_found = f.read()
    posts_found = posts_found.split("\n")
    posts_found = list(filter(None, posts_found))

while True:
    for submission in subreddit.new(limit=20):
        time.sleep(2)
        post_title = submission.title
        print("Checking post: " + post_title)
        for term in searchTerms:
            if term in post_title:
                time.sleep(2)
                if submission.id not in posts_found:
                    send_email("rfreemanh@gmail.com", "PC Part Alert", make_alert(term))
                    print("Email sent")
        else:
            pass
    with open("posts_found.txt", "w") as f:
        f.write(submission.id + "\n")