import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import  MIMEText

from email.mime.base import MIMEBase
from email import encoders

corpo = '<b>Bora toma uma</b>'
email = 'test@gmail.com'

#Lendo arquivo em binario
attachment = open('asmentoswine.jpeg', 'rb')

#Convertendo o arquivo em base64
att = MIMEBase('application', 'octet-stream')
att.set_payload(attachment.read())
encoders.encode_base64(att)
att.add_header('Content-Disposition', f'attachment; filename=asmentos.jpeg')


email_msg = MIMEMultipart()
email_msg['From'] = email
email_msg['To'] = email
email_msg['Subject'] = 'Olá'
email_msg.attach(MIMEText(corpo, 'html'))
email_msg.attach(att)



smt = smtplib.SMTP('smtp.gmail.com', 587)
smt.starttls()
smt.login(email, 'dfwhlvjwpskbmazm')
smt.sendmail(email_msg['From'], email_msg['To'],email_msg.as_string())
smt.quit()
