import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com', 25) #(provider, port)

server.ehlo()  #starts the service

#server.login('mail@mail.com', 'Pass123') #should not save in code encrypt in a txt file and pass
with open('password.txt', 'r') as f:
    password = f.read()

server.login('mail@mail', password)

msg = MIMEMultipart()
msg['From'] = 'Name'
msg['To'] = 'testmailz@spaml.de'  #test
msg['Subject'] = 'Just a test'

with open('message.txt', 'r') as f:     #message sent
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'moon.jpg'
attachment = open(filename, 'rb') #open the file

p = MIMEBase('application', 'octet-stream')  #attach file to payload
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')   #add attachment
msg.attach(p)   #add payload to msg

text = msg.as_string()
server.sendmail('mailtesting@mail.com', 'testmailz@spaml.de', text) #(email sending from, email sending to, what you are sending)