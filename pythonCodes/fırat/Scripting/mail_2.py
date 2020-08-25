import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path  # os.path e çok benziyor

html = Template(Path("./Scripting/index.html").read_text())

email = EmailMessage()
email["from"] = "Ali Fırat KUAS"
email["to"] = "af.kuas@gmail.com"
email["subject"] = "yılaaaaannnnn -- bu bir dolandırıcılık mesajıdır"

email.set_content(html.substitute(name="tintin"), "html")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("af.asimov@gmail.com", "thedarktower04")
    smtp.send_message(email)

    print("all good boiiii")
