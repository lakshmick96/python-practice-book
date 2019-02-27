# Write a function to compute the total number of lines of code in all python files in the specified directory recursively.

import os
def countlines(dir_name):
    count = 0
    for root, directories, filenames in os.walk(dir_name):
        for filename in filenames:
            if len(filename.split('.')) == 2 and filename.split('.')[1] == 'py':
                file_name = os.path.join(root,filename)
                f = open(file_name)
                count += len(f.readlines()) 
    return count



