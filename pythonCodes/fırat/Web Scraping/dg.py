import smtplib
from email.message import EmailMessage


class mailpushing():
    def __init__(self, mailfrom, mymailadress, mymailpassword, mailto, mailsubject, mailcontent, mailnumber):
        self.email = EmailMessage()
        self.email['from'] = mailfrom
        self.mymailadress = mymailadress
        self.mymailpassword = mymailpassword
        self.email['to'] = mailto
        self.email['subject'] = mailsubject

        self.email.set_content(mailcontent)

        with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(self.mymailadress, self.mymailpassword)
            smtp.send_message(self.email)
            for i in range(mailnumber):
                smtp.send_message(self.email)
                print('!!MAİL GÖNDERİLDİ')


mailpushing("DOGUHAN AYBARS AY", "doguhanaybars71@gmail.com",
            "Aybars1071.", "af.kuas@gmail.com", "konu", "içeçeöaödsapldöasd", 2)
