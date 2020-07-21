import os
import smtplib  # This module is defines an SMTP client session object that can be used to send mail 
import imghdr #This module determines the type of image contained in a file
from email.message import EmailMessage

#Grab the credentials from Environment Variables locally stored on your system
Email_id = os.environ.get('EMAIL_ID') #Sender's email address obtained 
Email_password = os.environ.get('EMAIL_PASSWORD') #Sender's password
Test_email_id = input("Enter Reciever Email") #Receiver's email

#For security purpose it is always recommended to grab the sender's email address and password from the system 
#However you can simply put in the creditials as strings to the variables if needed

#Craft the email
msg = EmailMessage() #Creating an email object
msg['Subject'] = 'Invitation for a Chat' #Subject of the message
msg['From'] = Email_id #Sender's email address
msg['To'] = Test_email_id #Receiver's email address
#For sending to multiple recievers,open a .csv file and read the email address in a list of strings and pass the list

msg.set_content('Hey! I wanted to ask you out for a chat over a bowl of sizzling brownies topped with chocolate ice-cream over this weekend')

#The names/paths of the images loaded in a list
files = ['assets/icecream.jpg','assets/pastry.jpg']

for file in files:
        with open(file,'rb') as f: #Make sure either the images/pdfs are in the same directory or the entire path is specified
            file_data = f.read()
            #Not required if we are sending pdfs
            file_type = imghdr.what(f.name) #used to determine the type of image
            file_name = f.name
        #Add the attachment to the message
        msg.add_attachment(file_data,maintype='image',subtype=file_type,filename=file_name)

#For using pdfs change: maintype = 'application' and sub_type='octet_stream'

#Set up SMTP Session over SSL
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp: 
    smtp.login(Email_id, Email_password) #Authentication
    smtp.send_message(msg) #Send the message

#If you are facing timeout-error for SSL and lack time then use the following
#Uncomment the following and delete the above SMTP Session
#with smtplib.SMTP('smtp.gmail.com', 587) as smtp: :
#     smtp.ehlo()
#     smtp.starttls()  # Encrypt the traffic using Tranport Layer Security
#     smtp.ehlo()
#     smtp.login(Email_id, Email_password) #Authentication
#     smtp.send_message(msg) #Send the message
