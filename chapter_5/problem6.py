# Write a function to compute the total number of lines of code, ignoring empty and comment lines, in all python files in the specified directory recursively.

import os
import re

def countlines(dir_name):
    count = 0
    for root, directories, filenames in os.walk(dir_name):
        for filename in filenames:
            if len(filename.split('.')) == 2 and filename.split('.')[1] == 'py':
                file_name = os.path.join(root,filename)
                f = open(file_name)
                lines = f.readlines()
                count += len(lines) 
                count -= lines.count('\n')
                for i in lines:
                    if re.search('#', i):
                        count -= 1

                
    return count


