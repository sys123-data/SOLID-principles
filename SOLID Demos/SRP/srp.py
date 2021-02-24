import sqlite3
from sqlite3 import Error

class User:
    def register_user(self, user_name, password, email):
        '''

        :param user_name: u
        :param password:
        :param email:
        commit sql
        '''
        connection = sqlite3.connect('sqldb.db')
        sql = f'insert into Users values ("{user_name}", "{password}","{email}" )'
        connection.execute(sql) # execute sql
        connection.commit()
        print(f'User Registered with {user_name} and {password}')

import syslog

class Logger:
    def write_log_to_system(self,message):
        syslog.syslog(syslog.LOG_ERR, message)

import json
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Email:
    def send_email(self, to_email, message_content, subject='User Registered'):

        with open('credentials.json', 'r') as f:
            data = json.load(f)


        smtp_server = 'smtp.gmail.com'
        port = 465
        sender_email = data["from_user"]
        password = data["password"]

        message = MIMEMultipart('alternative')

        message["From"] = sender_email
        message["To"] = to_email
        message["Subject"] = subject
        message_content = f'Hello, <br/><b>Message from TechnoAcademy: </b> <br/>' \
                          f'{message_content} <br/>All The Best <br/> Best Wishes, <br/>TechnoAcademy.net Support Team'
        part = MIMEText(message_content, 'html')

        message.attach(part)

        print(message)

        try:
            server =  smtplib.SMTP_SSL(smtp_server,port)
            server.ehlo()
            server.login(sender_email,password)
            server.sendmail(sender_email,to_email,message.as_string())
            server.close()
            print(f'Mail Sent to {to_email}')
        except:
            print('Something went wrong...')

class Registrations:
    def register_user(self, user_name, password, email):
        try:
            User().register_user(user_name,password,email)

        except Exception:
            Logger().write_log_to_system('Error While Registering User')
            return
        try:

            Email().send_email(to_email=email, message_content='You have Successfully Registered')
            print(4)
        except Exception:
            print('Email not sent')
            return

r = Registrations()
# remember that username is primary key
r.register_user('ab1','parola','georgecristiangtrxd@gmail.com')

'''
I think that the GMail SMTP server does a reverse DNS lookup 
on the IP address that you connect from, and refuses the connection 
if no domain can be found. This is to avoid spammer 
from using their SMTP server as an open relay.
'''

'''
A Table can have a Composite Primary Key which is a primary key made from two or more columns. For example:

CREATE TABLE userdata (
  userid INT,
  userdataid INT,
  info char(200),
  primary key (userid, userdataid)
);
Update: Here is a link with a more detailed description of composite primary keys.
https://weblogs.sqlteam.com/jeffs/2007/08/23/composite_primary_keys/
'''