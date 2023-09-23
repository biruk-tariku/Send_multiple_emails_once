import smtplib as s

ob = s.SMTP("smtp.gmail.com", 587)
ob.ehlo()
ob.starttls()
ob.login("biruktariku13@gmail.com", "BT1234BT")
subject = "Hello"
body = "testing the code"
message = "subject:{}\n\n{}".format(subject, body)
listadd = ["birukyetariku12@gmail.com", "biruktariku02@gmail.com"]
ob.sendmail("biruktariku13@gmail.com", listadd, message)
print("send mail")
ob.quit()
