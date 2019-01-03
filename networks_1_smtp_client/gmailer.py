from Smtp_client import *


def cli_send():
    hostname = input("hostname: ")
    port = int(input("port: "))
    adress = input("adress: ")
    password = input("password: ")
    rcpt = input("to: ")
    subject = input("subject: ")
    message = ""
    t = ""
    print("type your message, to finish type \".\" and hit enter")
    while(t != "."):
        t = input()
        message += "\n" + t    
    mailer = Smtp_client(hostname, port, adress, password)
    mailer.sendmail(rcpt, subject, message)


def send_defualt_account():
    hostname = "smtp.gmail.com"
    port = 465
    adress = "smtp3148@gmail.com"
    password = "send1234"
    rcpt = "smtp3148@gmail.com"
    subject = input("subject: ")
    message = ""
    t = ""
    print("type your message, to finish type \".\" and hit enter")
    while(t != "."):
        t = input()
        message += "\n" + t   
    mailer = Smtp_client(hostname, port, adress, password)
    mailer.sendmail(rcpt, subject, message)

    
def send_test():
    hostname = "smtp.gmail.com"
    port = 465
    adress = "smtp3148@gmail.com"
    password = "send1234"
    rcpt = "smtp3148@gmail.com"
    subject = "just a subject"
    message = "but \r\n not \r just \n any message"         
    mailer = Smtp_client(hostname, port, adress, password)
    mailer.sendmail(rcpt, subject, message)

    
def conection_test():
    hostname = "smtp.gmail.com"
    port = 465
    adress = "smtp3148@gmail.com"
    password = "send1234"
    rcpt = "smtp3148@gmail.com"
    subject = "just a subject"
    message = "but not just any message"         
    mailer = Smtp_client(hostname, port, adress, password)
    
    
send_defualt_account()
