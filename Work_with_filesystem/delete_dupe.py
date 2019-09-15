import os

class Delete(object):
    #delete metods for file type objects
    
    def __init__(self, file):
        self.file = file
        
        
        
    def interactive(self):
        #interactive delete
        input = raw_input('Do you really want to delete %s? [N]/Y: ' % self.file)
        if input.upper() == 'Y':
            print 'DELETING: %s' % self.file
            status = os.remove(self.file)
        else:
            print 'Skipping: %s' % self.file
        
        return status
    
    
    
    def dryrun(self):
        #del imitation
        print "Dry Run: %s [NOT DELETED]" % self.file
        return
    
    
    
    def delete(self):
        #delete files without additional conditions
        print 'DELETING: %s' % self.file
        try:
            status = os.remove(self.file)
        except Exception, err:
            print err
            
        return status
    
    
    
if __name__ == '__main__':
    from duplicate_search import findDupes
    dupes = findDupes('/your/path')
    for dupe in dupes:
        delete = Delete(dupe)
        #delete.dryrun()
        #delete.delete()
        delete.interactive()
    
