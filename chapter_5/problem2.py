#Write a program that takes one or more filenames as arguments and prints all the lines which are longer than 40 characters.

def readfiles(filenames):
    for f in filenames:
        for line in open(f):
            if len(line) > 40:
                print line


