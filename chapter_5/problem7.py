#Write a program split.py, that takes an integer n and a filename as command line arguments and splits the file into multiple small files with each having n lines.

import sys
f = open(sys.argv[2], 'r')
n = int(sys.argv[1])
lines = f.readlines()
start = 0
end = n
count = 0
while end <= len(lines):
    with open('file_%d' %count, 'w') as f:
        for i in range(start,end):
            f.write(lines[i])
    count += 1
    start += n
    end += n



