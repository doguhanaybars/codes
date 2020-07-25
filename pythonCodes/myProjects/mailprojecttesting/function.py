import smtplib
from email.message import EmailMessage


def mailfunction(mailfrom, mymailadress, mymailpassword, mailto, mailsubject, mailcontent, mailnumber):
    email = EmailMessage()
    email['from'] = mailfrom
    email['to'] = mailto
    email['subject'] = mailsubject

    email.set_content(mailcontent)

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(mymailadress, mymailpassword)
        smtp.send_message(email)
        for i in range(mailnumber):
            smtp.send_message(email)
            print('!!MAİL GÖNDERİLDİ')
# mailfunction('İsim-Soyisim','kendi mailin','mailşifren','gönderilen mail adresi','Konu Başlığı','içerik',kaç kere göndereceğin )
# mailfunction('Mehmet Yılmaz','mehmetyilmaz@gmail.com','mehmet123','ayseyilmaz@gmail.com','Konu Başlığı','içerik',4)