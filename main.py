import smtplib
from email.message import EmailMessage

email= EmailMessage()
email['from'] = 'name of person'
email['to'] = "send to email"
email['subject'] ="Learning Python did you get this email?"

email.set_content("I am try to figure out this Python language")

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("email@email.com", "email_password")
    smtp.send_message(email)
    #print("all good")

