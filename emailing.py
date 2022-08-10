import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from password import password


msg = MIMEMultipart()

with open('mail_body.txt') as file:
    message = file.read()

password = password
msg['From'] = "zhydykalex@ukr.net"
msg['To'] = "alex11m@ukr.net"
msg['Subject'] = "Avenga test task Alexandr Zhydyk"

# add in the message body
msg.attach(MIMEText(message, 'plain'))

with open('final/taxi_report.csv') as file:
    attachment = MIMEText(file.read())

attachment.add_header('content-disposition', 'attachment', filename='taxi_report.csv')
msg.attach(attachment)

server = smtplib.SMTP_SSL('smtp.ukr.net', 465)

server.login(msg['From'], password)

server.sendmail(msg['From'], msg['To'], msg.as_string())

server.quit()