from subprocess import call
import sys
import time
import smtplib

#this code will try synchronize 2 dirs, until it done and send message on your gmail
#youhave to allow access for this app in your google account setings

source = '/path/to/sync_dir_A/' #Note the trailing slash
target = '/path/to/sync_dir_B'
rsync = 'rsync'
arguments = '-av'
cmd = '%s %s %s %s' % (rsync, arguments, source, target)

def sync():
    while True:
        ret = call(cmd, shell=True)
        if ret != 0:
            
            print 'resubmitting rsync'
            time.sleep(30)
        else:
            print 'rsync was succesful'
            port = 465
            smtp_server = 'smtp.gmail.com'
            sender_email = 'sender@gmail.com'
            receiver_email = 'receiver@gmail.com'
            password = 'yourpswd'
            message = 'Your message text here.'
            
    
            server = smtplib.SMTP_SSL(smtp_server, port) 
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
            server.quit()            
            sys.exit(1)
            
sync()
