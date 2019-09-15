from subprocess import call
import sys
import time
import smtplib

#this code will try synchronize 2 dirs, until done!

source = '/tmp/sync_dir_A/' #Note the trailing slash
target = '/tmp/sync_dir_B'
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
            sender_email = 'romadnestr@gmail.com'
            receiver_email = 'adalllinincorp@gmail.com'
            password = 'byjq1234gfhjkmxbr'
            message = 'Message from vselosi.'
            
    
            server = smtplib.SMTP_SSL(smtp_server, port) 
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
            server.quit()            
            sys.exit(1)
            
sync()