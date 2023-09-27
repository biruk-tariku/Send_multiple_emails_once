# Send_multiple_email_once_using_python

a Python script that uses the `smtplib` library to send an email via a Gmail SMTP server. Here's an explanation of what the code does:

1. Import the `smtplib` library as `s`.

2. Create an SMTP object `ob` and connect to the Gmail SMTP server at "smtp.gmail.com" on port 587 (TLS encryption).

3. Use the `ehlo()` method to identify the client to the server.

4. Start a TLS (Transport Layer Security) connection with the `starttls()` method to encrypt the communication.

5. Log in to your Gmail account using the `login()` method with your email address and password.

6. Define the email subject and body.

7. Create the email message by formatting the subject and body using string formatting.

8. Create a list of recipient email addresses in `listadd`.

9. Use the `sendmail()` method to send the email. It takes three arguments:
   - Sender's email address ("example@gmail.com")
   - List of recipient email addresses (`listadd`)
   - The formatted email message

10. Print "send mail" to indicate that the email has been sent.

11. Finally, use the `quit()` method to close the SMTP connection.

Make sure to replace `"example@gmail.com"` and `"example pass"` with your actual Gmail email address and password, respectively. Also, ensure that you have allowed less secure apps to access your Gmail account or have generated an "App Password" if you have two-factor authentication enabled for your Google account.
