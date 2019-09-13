import tarfile, sys


try:
    #open tar-file
    tar = tarfile.open(sys.argv[1], 'r:tar')
    #menu and save the choice
    selection = raw_input('Set\n\
    1 - extract file\n\
    2 - show information\n\
    3 - show all files in archive\n\n')
    #execution based on your choice
    if selection == '1':
        filename = raw_input('Set filename for extraction: ')
        tar.extract(filename)
    elif selection == '2':
        filename = raw_input('Set file name for view: ')
        for tarinfo in tar:
            if tarinfo.name == filename:
                print '\n\
                File name: \t\t', tarinfo.name, '\n\
                Size: \t\t', tarinfo.size, 'bites\n'
    elif selection == '3':
        print tar.list(verbose=True)
except:
    print 'Error while executing program!'