# Implement a program dirtree.py that takes a directory as argument and prints all the files in that directory recursively as a tree.

import sys, os
path = sys.argv[1]
count = 0
print (path.split('/')[-1]) + '/'
def print_file(newpath):
    global count
    if newpath == '':
        newpath = path
    for i in os.listdir(newpath):
	if os.path.isdir(newpath+'/'+i):
	    print (count* '| ')+'|--'+ i +'/'
            newpath = path+'/'+i
            count += 1
            print_file(newpath)
        else:
	    print (count*'| ')+ '|--'+i
    count = 0

            
print_file(path)

