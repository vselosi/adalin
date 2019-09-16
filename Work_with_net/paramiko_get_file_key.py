import paramiko
import os

hostname = 'localhost'
port = 22
username = 'root'
password = 'toor'
dir_path = '/path/to/file'
pkey_file = '/path/to/.ssh/id_rsa'

if __name__ == '__main__':
    pkey = paramiko.RSAKey.from_private_key_file(pkey_file)
    t = paramiko.Transport((hostname, port))
    t.connect(username=username, pkey=pkey)
    sftp = paramiko.SFTPClient.from_transport(t)
    files = sftp.listdir(dir_path)
    for f in files:
        print 'Retrieving', f
        sftp.get(os.path.join(dir_path, f), f)
    t.close()
        