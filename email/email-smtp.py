import smtplib
from email.mime.text import MIMEText

email, senha = 'test@gmail.com', 'dfwhlvjwpskbmazm'
menssagem = MIMEText('Test','plain', 'utf-8')

smtobj = smtplib.SMTP('smtp.gmail.com', 587)
print(smtobj.starttls())
print(smtobj.login(email, senha))
print(smtobj.sendmail(email, email, f'Subject:Goku\n{menssagem}'))
