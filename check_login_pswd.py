import pwd

    
#counter
erroruser = []
errorpass = []
#get pswd base
passwd_db = pwd.getpwall()

try:
    for entry in passwd_db:
        username = entry[0]
        password = entry[1]
        if len(username) < 7:
            erroruser.append(username)
        if len(password) < 10:
            errorpass.append(username)
            
        #stdout result
        print 'This users have usernames less then 7 characters: '
        #print erroruser
        for i in erroruser:
            print i
            
        print '\nThis users have password less then 10 characters: '
        #print errorpass
        for i in errorpass:
            print i
except:
    print 'Error while executing program!'
    
