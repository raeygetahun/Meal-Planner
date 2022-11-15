from email import message
from email.message import EmailMessage
import smtplib
from planner import *


def emailto(address):
    email="mealplanfromraey@gmail.com"
    password="pythonisgreatA1"

    emailmessage=EmailMessage()

    emailmessage['Subject']="Weekly Meal Plan"
    emailmessage['From']=email
    # emailmessage['To']=email

    emailmessage.set_content('\n\n'.join([item for item in mealplan]))


    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,address,emailmessage)
    print("sent")

# with smtplib.SMTP_SSL('smtp.gmail.com',587) as smtp:
#     smtp.login(email,password)
#     smtp.send_message(emailmessage)


