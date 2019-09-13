#serach files and show access rights 
import stat, sys, os, string, commands


try:
    pattern = raw_input('Set searching pattern:\n')
    
    
    commandString = 'find ' + pattern
    commandOutput = commands.getoutput(commandString)
    findResults = string.split(commandOutput, '\n')
    
    
    print 'Files: '
    print commandOutput
    print'-----------------------------------------'
    for file in findResults:
        mode = stat.S_IMODE(os.lstat(file)[stat.ST_MODE])
        print '\nPermission for file ', file, ':'
        for level in 'USR', 'GRP', 'OTH':
            for perm in 'R', 'W', 'X':
                if mode & getattr(stat, 'S_I'+perm+level):
                    print level, 'have ', perm, 'access rights'
                else:
                    print level, "don't have ", perm, 'access rights'
except:
    print 'Got a problem! Check message above.'