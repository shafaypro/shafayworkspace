import os
import os2emxpath
import sys
import types
class Parent():
    def name(self):
        print ('This is parent Process')
    def ProcessCreate(self):
        Parentprocess=os.fork()
        return Parentprocess
class Child():
    def name(self):
        print ('This is parent child')
currDir = os.curdir
print ('You current directory is '+str(currDir))
#Mapping in python is indicated by:
s=os.environ
print(s) # This return the specific path of the envirement in HomeDirectory
#parent_id=os.getpid()
#print (parent_id)
#shafay=os.fork()
shafay=os.Fork()
if shafay< 0:
    print ('Process is not created')
else:
    print ('Process created')
import time
time.sleep(2)