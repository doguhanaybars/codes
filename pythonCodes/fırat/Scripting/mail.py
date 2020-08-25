import smtplib
from email.message import EmailMessage

email = EmailMessage()
email["from"] = "Ali Fırat KUAS"
email["to"] = "doguhanaybars71@gmail.com"
email["subject"] = "yılaaaaannnnn -- bu bir dolandırıcılık mesajıdır"

email.set_content(" ilerliyoruz biladerim. ")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("af.asimov@gmail.com", "thedarktower04")
    smtp.send_message(email)

    print("all good boiiii")
