import sqlite3
import  re
conn = sqlite3.connect('assignment2.sqlite')
cur = conn.cursor() # to send the command to the sql server
cur.execute('''Drop table If exists Counts''')
cur.execute('''
CREATE TABLE Counts(org TEXT,count INTEGER)
''')
fname=raw_input('Enter the name of the File')
if (len(fname)< 1): fname='mbox-short.txt'
fh= open (fname)
for line in fh:
    line=line.strip()
    line = line.rstrip()
    if not line.startswith('From: '): continue
    #pieces = line.split()
    element=re.findall('@([a-z0-9A-Z]+\.[a-z0-9A-Z]+\S+)',line)
    for org in element:
        org=org.rstrip()
        cur.execute('Select count from Counts where org = ?',(org, ))
        try:
            count=cur.fetchone()[0]  #checking the fetching if the statment already exist there
            cur.execute('Update Counts Set count = count + 1 where org = ?',(org,))
        except:
            cur.execute('''Insert into Counts(org,count) Values (?,1)''',(org,))
conn.commit()  #commit the sql transaction // you need to let it outside ofthe loop

sqlstr='Select org,count from Counts Order By count Desc '

for row in cur.execute(sqlstr):
    print (str(row[0]),row[1])   #Count of the number of row else let it be 1
cur.close()  # closing hte data base