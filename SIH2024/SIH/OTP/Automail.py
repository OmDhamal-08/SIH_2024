import smtplib
from email.message import EmailMessage
import time
import schedule
import psutil
import os

def GetProcessInfo():
    listprocess = []    
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        listprocess.append(proc.info)
    
    return listprocess

def attach_file_to_email(email, filename):
    with open(filename, 'rb') as f:
        file_data = f.read()
        file_name = os.path.basename(filename)
    email.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

def creatlog(filename="Marvellous.txt"):
    seprator="-"*70
    fd=open(filename,"a")
    fd.write(seprator+"\n")
    fd.write("Marvellous Log File"+"\n")
    fd.write(seprator+"\n")
    fd.write("Created at:"+time.ctime()+"\n")
    fd.write(seprator+"\n")
    arr=GetProcessInfo()
    for i in arr:
        fd.write("%s \n"%i)
    fd.write(seprator+"\n") 
    fd.close()

def Mail_Sender():
    print("Application run at:",time.ctime())
    email = EmailMessage()
    email.set_content("Hello")

    email["Subject"] = "Test Email"
    email["From"] = "omdhamal665@gmail.com"
    email["To"] = "19cravey@gmail.com"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("vgu8874@gmail.com", "waxj yrqh wgdu lwtm")
    creatlog()
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