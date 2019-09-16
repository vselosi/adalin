import paramiko
import os

hostname = '192.168.1.15'
port = 22
username = 'root'
password = 'toor'
dir_path = '/path/to/dir'

if __name__ == '__main__':
    t = paramiko.Transport((hostname, port))
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    files = sftp.listdir(dir_path)
    for f in files:
        print 'Retrieving', f
        sftp.get(os.path.join(dir_path, f), f)
        # use put() insted of get() you want to trasport file
    t.close()