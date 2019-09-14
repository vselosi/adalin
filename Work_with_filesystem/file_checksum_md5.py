import hashlib

def create_checksum(path):
    #read file. compute file's control sum, string by string
    #return control sum for total file
    
    fp = open(path)
    cheksum = hashlib.md5()
    while True:
        buffer = fp.read()
        if not buffer:
            break
        cheksum.update(buffer)
        fp.close()
        checksum = cheksum.digest()
        return checksum
