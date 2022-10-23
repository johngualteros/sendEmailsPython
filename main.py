import smtplib
from decouple import config

email = input('Please Enter your email: ')
message = input('Please Enter the body of email: ')
subject = input('Please Enter the subject of email: ')

message = 'Subject: {}\n\n{}'.format(subject, message)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('gualterosjohn40@gmail.com', 'passwordApp')

server.sendmail(email, 'gualterosjohn40@gmail.com', message)

server.quit()
