import smtplib
from email.message import EmailMessage

email = EmailMessage()
email["from"] = "Ali Fırat KUAS"
email["to"] = "doguhanaybars71@gmail.com"
email["subject"] = "yılaaaaannnnn -- bu bir dolandırıcılık mesajıdır"
name = ["fırat", "doğu", "kaan", "berk", "veysel",
        "ahmet", "mehmet", "samet", "doğuhan", "şevket"]


with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("af.asimov@gmail.com", "thedarktower04")
    deneme = 1
    for i in name:
        email.set_content(f"{i} ilerliyoruz biladerim. ")
        smtp.send_message(email)
        print(f"{deneme}. deneme")
        deneme += 1

    print("all good boiiii")
