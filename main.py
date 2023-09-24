import smtplib as s

ob = s.SMTP("smtp.gmail.com", 587)
ob.ehlo()
ob.starttls()
ob.login("example@gmail.com", "example pass")
subject = "Hello"
body = "testing the code"
message = "subject:{}\n\n{}".format(subject, body)
listadd = ["example_123@gmail.com", "example2202@gmail.com"]
ob.sendmail("example@gmail.com", listadd, message)
print("send mail")
ob.quit()
