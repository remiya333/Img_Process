import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Rems'
email['to'] = 'remiya.nadar@ext.saint-gobain.com'
email['subject'] = 'You won 100000 dollars!'

email.set_content(html.substitute({'name':'Tintin'}),'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('remiya333@gmail.com','Jesus@333')
    smtp.send_message(email)
    print('all done!')