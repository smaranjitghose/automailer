<h1 align ='center'>AutoMailer 📧</h1>

A crisp python script to send emails using [SMTP](https://tools.ietf.org/html/rfc821.html)
<p align = 'center'><img src = "https://media.giphy.com/media/Qw4X3Fsf0N1VqFFUiBi/giphy.gif" width = 40%></p>

<h2 align ='center'>Usage</h2>

<p align = 'center'><img src = "https://media.giphy.com/media/3Xw6TZ8xgjqojOwlvr/giphy.gif" width = 50%></p>

Here you go:

- Clone or Download this repository ⏬
- Open the Terminal 🐱‍💻
- Move inside 👉 the repo 
```cd automailer``` 
- Put your image inside the repo or get its path
- Now make sure you have all the dependencies🧱 
  ```pip install -r requirements.txt```
- Open the script and do the following changes

  - Set ```Email_id``` to the your email address
  - Set ```Email_password``` to the password of your aforementioned email address
  
  ^^ Its a nice practice to have them saved as Environment variables in the system but not mandatory
  
  - Set ```Test_Email_id``` to the reciever's email address
  - Set ```msg['Subject']``` to the Subject of your Email
  - Set ```msg.set_content=()``` to the body of your Email.(You even use an HTML format for this)
  - Set ```files =``` to the list of file names(either images or pds) to be sent as attachment
  
 
   Make sure the files to be sent are in the same directory as the script otherwise specify entire path
  - For sending PDFs instead  as attachments change: ```maintype = 'application' ``` and ```sub_type = 'octet_stream'```
- Save the script
- Open the terminal and cd in to directory 
- Execute the command: ```python automailer.py```
- Bam! your email is sent within the blink of an eye 


<h2 align ='center'>Suggestions: ⚠</h2>
<p align = 'center'><img src = "https://media.giphy.com/media/8qJov1TOy2hI4/giphy.gif" width = 30%></p>

- Don't save the script as ```email.py```
- Make sure your Google Account has [Allow Less Secure App Access](https://myaccount.google.com/lesssecureapps) enabled
- At times setting up the SSL might fall into timeout. Don't panic. Just reconnect or connect to a new network and try
- If SSL is still timed out and its urgent, simply use TTL for connection (Instructions given at the end of the script)


<h2 align ='center'>Further Work</h2>

- Read a set of email ids from a csv file
- Try using the same script for other email providers like [Protonmail](protonmail.com),[Outlook](https://outlook.live.com/owa/),etc
- Modify the script to send both PDFs and Images simultaneously as attachments
- Modify the script to read the subject from user
- Modify the script to read the content from  a content.txt file
- Create GUI for the script using [Tkinter](https://docs.python.org/3.8/library/tkinter.html), [Kivy](https://kivy.org/#home) or [PyQt](https://www.riverbankcomputing.com/static/Docs/PyQt5)

<h2 align = 'center'>License 📜</h2>
<p align = 'center'><img src = 'https://media.giphy.com/media/XfD8VJDUurgMjNEP72/giphy.gif' width = 40%></p>

[MIT License](https://github.com/smaranjitghose/automailer/master/LICENSE)

  

 
