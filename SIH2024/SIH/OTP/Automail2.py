import smtplib
from email.message import EmailMessage
import time
import schedule
import psutil
import os

def attach_file_to_email(email, filename):
    with open(filename, 'rb') as f:
        file_data = f.read()
        file_name = os.path.basename(filename) # this function use to extract the 
    email.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

def Mail_Sender():
    print("Application run at:",time.ctime())
    email = EmailMessage()
    email.set_content("Hello")

    email["Subject"] = "Test Email"
    email["From"] = "omdhamal665@gmail.com"
    email["To"] = "vaibhavkhangale15@gmail.com"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("vgu8874@gmail.com", "waxj yrqh wgdu lwtm")
    fname="Marvellous.txt"
    attach_file_to_email(email,fname)
    server.send_message(email)
    server.quit()
    print("Mail send at:",time.ctime())
    print("Email sent successfully!")
def main():
    schedule.every(1).minutes.do(Mail_Sender)
    while True:
        schedule.run_pending()
        time.sleep(1)
if __name__ == "__main__":
    main()