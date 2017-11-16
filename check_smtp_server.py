### PROGRAM : Python program to check whether an SMTP Server exists for sending email
### PROGRAMMED BY : SUMAN GANGOPADHYAY
### DATE : 16-Nov-2017
import smtplib
import time
def CheckSmtpServer(smtp_url, smtp_port):
    try:
        smtpobj = smtplib.SMTP(smtp_url, smtp_port);
        if (type(smtpobj)):
            return 1;
    except TimeoutError:
        return 0;

if(CheckSmtpServer("smtp.gmail.com", 587) == 1):
    print("SMTP server exists");
else:
    print("SMTP server does not exists");





