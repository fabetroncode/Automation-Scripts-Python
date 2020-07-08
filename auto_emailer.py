import smtplib

#variables
sender_addr = input('Enter in the email you are sending from.')
reciever_addr = input('enter who you want to receive this email')
#if you have problems with smtp port try ex: smtp.gmail.com:port
host = 'smtp.gmail.com'
port = 587 #ssl port is 587, 25 is w/o SSL

message = """\
Subject: Some subject

This is an email sent from a program
"""

def mailer(sender, receiver, email_message, host):
    try:
        with smtplib.SMTP(host, port) as server:
            server.ehlo()
            server.starttls()
            server.sendmail(sender,receiver,message)
    except ValueError:
        print('exit code 1')


