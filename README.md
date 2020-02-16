# PyMailer 
A crisp python script to send emails using [SMTP](https://tools.ietf.org/html/rfc821.html)

## Usage: 
- Download the PyMailer.py script
- Make sure you have the pdfs/images to be sent in the same directory
- Open the script and do the following changes

  - Set ```Email_id``` to the your email address
  - Set ```Email_password``` to the password of your aforementioned email address
  
  Its a nice practice to have them saved as Environment variables in the system but not mandatory
  
  - Set ```Test_Email_id``` to the reciever's email address
  - Set ```msg['Subject']``` to the Subject of your Email
  - Set ```msg.set_content=()``` to the body of your Email.(You even use an HTML format for this)
  - Set ```files =``` to the list of file names(either images or pds) to be sent as attachment
  
 
   Make sure the files to be sent are in the same directory as the script otherwise specify entire path
  - For sending PDFs instead  as attachments change: ```maintype = 'application' ``` and ```sub_type = 'octet_stream'```
- Save the script
- Open the terminal and cd in to directory 
- Execute the command: ```python PyMailer.py```
- Bam! your email is sent within the blink of an eye 

## Suggestions:
- Don't save the script as ```email.py```
- Make sure your Google Account has [Allow Less Secure App Access](https://myaccount.google.com/lesssecureapps) enabled
- At times setting up the SSL might fall into timeout. Don't panic. Just reconnect or connect to a new network and try
- If SSL is still timed out and its urgent, simply use TTL for connection (Instructions given at the end of the script)

## Further work:
- Read a set of email ids from a csv file
- Try using the same script for other email providers like [Protonmail](protonmail.com),[Outlook](https://outlook.live.com/owa/),etc
- Modify the script to send both PDFs and Images simultaneously as attachments
- Modify the script to read the subject from user
- Modify the script to read the content from  a content.txt file
- Create GUI for the script using [Tkinter](https://docs.python.org/3.8/library/tkinter.html), [Kivy](https://kivy.org/#home) or [PyQt](https://www.riverbankcomputing.com/static/Docs/PyQt5)
  

 
