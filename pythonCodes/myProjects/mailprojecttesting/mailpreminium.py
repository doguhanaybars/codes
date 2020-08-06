# from PyQt5 import QtWidgets
# import sys
# from mproject import Ui_MainWindow
# from function import mailfunction


# class MyApp(QtWidgets.QMainWindow):

#     def __init__(self):
#         super(MyApp,self).__init__()
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
        
        
#         self.ui.lineEdit   = myname
#         self.ui.lineEdit_2 = mymail
#         self.ui.lineEdit_7 = mypassword
#         self.ui.lineEdit_3 = tomail
#         self.ui.lineEdit_4 = mailsubject
#         self.ui.lineEdit_5 = mailcontent
#         self.ui.lineEdit_6 = mailnumber
        
        
#         self.ui.pushButton.clicked.connect(self.hesapla)
        
#     def hesapla(self):
           
#         mailfunction(myname,mymail,mypassword,tomail,mailsubject,mailcontent,int(mailnumber))
        


# def app():
#     app = QtWidgets.QApplication(sys.argv)
#     win = MyApp()
#     win.show()
#     sys.exit(app.exec_())

# app()

import smtplib
from email.message import EmailMessage

class mailpushing():
    def __init__ (self,mailfrom, mymailadress, mymailpassword, mailto, mailsubject, mailcontent, mailnumber):
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


# mailpushing('Doğuhan Aybars Ay','ornekmail@gmail.com','Password.','Karsımail@gmail.com','class deneme','içerik',2)