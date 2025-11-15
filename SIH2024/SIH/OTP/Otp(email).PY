import smtplib
from email.message import EmailMessage
import time
import schedule
import psutil
import os
import random 

def otp_generate():
    return str(random.randint(1000, 9999))

def Mail_Sender():
    with open("email.txt","r") as fi:
        f=fi.readline()
    print("Application run at:",time.ctime())
    email = EmailMessage()
    email['Subject'] = 'OTP for login'
    OTP=otp_generate()
    email.set_content("This mail is from organization.%s your One Time Password (OTP)"%OTP)
    email["From"] = "vgu8874@gmail.com"
    email["To"] = f
    server = smtplib.SMTP("smtp.gmail.com", 587)
    #smpt stands for simple mail transfer protocole
    server.starttls()
    server.login("vgu8874@gmail.com", "waxj yrqh wgdu lwtm")
    server.send_message(email)
    email.set_content("Otp is valid upto 30 sec")
    print("Mail send at:",time.ctime())
    print("Email sent successfully!")
    time.sleep(30)
    valid_opt(OTP)
    server.quit()

def valid_opt(OTP):
    with open("otp.txt","r") as f1:
        op=f1.readline()
    if(OTP==op):
        print("OTP is valid")
    else:
        print("OTP is invalid")

def main():
    Mail_Sender()
if __name__ == "__main__":
    main()