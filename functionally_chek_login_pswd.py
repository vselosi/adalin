import pwd

passwd_db = pwd.getpwall()



def erroruser():
    erroruser = []
    global passwd_db
    try:
        for entry in passwd_db:
            username = entry[0]
            if len(username) < 7:
                erroruser.append(username)
    except:
        print 'Error while executing erroruser function!'
    print 'This users have username less then 7 characters: \n'  
    return  erroruser



def errorpass():  
    errorpass = []
    global passwd_db
    try:
        for entry in passwd_db:
            password = entry[0]
            if len(password) < 10:
                errorpass.append(password)
    except:
        print 'Error while executing errorpass function!'
    print 'This users have password less then 7 characters: \n'   
    return errorpass



print erroruser()
print errorpass()
