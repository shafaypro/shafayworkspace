import re
import string
fopen = open ('mbox-short.txt','r')
lines=fopen.readlines()
for line in lines:
    line = line.rstrip()
    if line.startswith('From '):
        element=re.findall('@[a-z0-9]+\.[a-z0-9]+\S+',line)
        for r in element:
            print r