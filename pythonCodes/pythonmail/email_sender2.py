import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path 

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Doğuhan Aybars Ay'
email['to'] ='af.asimov@gmail.com'
email['subject'] = 'HAYDAAAAAA'

email.set_content(html.substitute({'name': 'Fırat'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('mailadresim','şifrem.')
    smtp.send_message(email)
    print('all good boos!')
    