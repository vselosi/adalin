#connect yo SSH and execute the 'ifconfig' command

import paramiko

hostname = '192.168.0.1'
port = 22
username = 'root'
password = 'passsword'

if __name__ == '__main__':
    paramiko.util.log_to_file('paramiko.log')
    s = paramiko.SSHClient()
    s.load_system_host_keys()
    s.connect(hostname, port, username, password)
    stdin, stdout, sterr = s.exec_command('ifconfig')
    print stdout.read()
    s.close()
    
    