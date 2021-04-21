# Program name: 
# Your Name: Aerin Schmall
# Python Version: 3.7.8
# Date Started - Date Finished: //2020 - //2020
# Description: 
import smtplib as sm
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = sm.SMTP('smtp.gmail.com', 465)

server.ehlo()
server.login('djvk6933@gmail.com', 'If0rg0tit')

msg = MIMEMultipart()
msg['From'] = 'djvk'
msg['To'] = 'djvk95037@gmail.com'
msg['Subject'] = 'test'
msg.attach(MIMEText('testign', 'plain'))

text = msg.as_string()
server.sendmail('djvk6933@gmail.com', 'djvk95037@gmail.com')
print('sent')
'''
============= RESTART: C:\\Users\\aerin\\Documents\\Python\\
'''
