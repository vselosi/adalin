import os


class diskwalk(object):
    
    
    #collections access interfase
    def __init__(self, path):
        self.path = path
        
    
    
    def enumeratePaths(self):
        #return paths for all files in dir as list
        path_collection = []
        for dirpath, dirnames, filenames in os.walk(self.path):
            for file in filenames:
                fullpath = os.path.join(dirpath, file)
                path_collection.append(fullpath)
                
        return path_collection
    
    
    
    def enumerateFiles(self):
        #return file's names in dir as list
        file_collection = []
        for dirpath, dirnames, filenames in os.walk(self.path):
            for file in filenames:
                file_collection.append(file)
                
        return file_collection
    
    
    
    def enumerateDirs(self):
        #return subdir's names in dir as list
        dir_collection = []
        for dirpath, dirnames, filenames in os.walk(self.path):
            for dir in dirnames:
                dir_collection.append(dir)
                
        return dir_collection