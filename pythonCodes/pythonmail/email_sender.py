import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Doğuhan Aybars Ay'
email['to'] ='af.asimov@gmail.com'
email['subject'] = 'HAYDAAAAAA'

email.set_content('Haydi bakalım')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('mailadresim','şifrem.')
    smtp.send_message(email)
    print('all good boos!')
    