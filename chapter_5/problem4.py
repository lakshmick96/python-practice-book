#Write a function to compute the number of python files (.py extension) in a specified directory recursively.

import os
def pythonfiles(dir_name):
    count = 0
    for root, directories, filenames in os.walk(dir_name):
        for filename in filenames:
            if len(filename.split('.')) == 2 and filename.split('.')[1] == 'py':
                count += 1 
    return count

