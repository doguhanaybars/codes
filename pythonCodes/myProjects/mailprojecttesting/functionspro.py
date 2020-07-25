from function import mailfunction
        
def functionpro():
    myname = str(input('Adınız Soyadınız: '))
    mymail = str(input('Mail Adresiniz: '))
    mypassword = str(input('Mail Adresinizin Şifresi: '))
    tomail = str(input('Karşı Tarafın Mail Adresi: '))
    mailsubject = str(input('Konu Başlığı: '))
    mailcontent = str(input('Mesajınız: '))
    mailnumber = int(input('Kaç Kere Mail Gönderilsin: '))
    mailfunction(myname,mymail,mypassword,tomail,mailsubject,mailcontent,mailnumber)

functionpro()