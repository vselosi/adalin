from file_checksum_md5 import create_checksum
from dir_traversal_module import diskwalk
from os.path import getsize

path = '/root/Documents/System_admin'

def findDupes(path=path):
    dup = []
    record = {}
    d = diskwalk(path)
    files = d.enumeratePaths()
    for file in files:
        compound_key = (getsize(file), create_checksum(file))
        if compound_key in record:
            dup.append(file)
        else:
            print 'Creating compound key record:', compound_key
            record[compound_key] = file
    
    return dup

if __name__ == '__main__':
    dupes = findDupes()
    for dup in dupes:
        print 'Duplicate: %s' % dup