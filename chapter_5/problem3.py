#Write a function findfiles that recursively descends the directory tree for the specified directory and generates paths of all the files in the tree.

import os
def findfiles(dir_name):
    for root, directories, filenames in os.walk(dir_name):
        for filename in filenames:             
             print os.path.join(root,filename) 
findfiles('/home/lakshmi/Documents')
            
