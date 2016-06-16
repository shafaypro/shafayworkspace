import os
def child():
    print ('\n A new Child',os.getpid())
    os._exit(0)
def parent():
    while True:
        newpid=os.fork()
        if newpid == 0:
            child()
        else:
            pids=(os.getpid(),newpid)
            print ("parent : %d , child : %d\n" %pids)
            reply=input('q for quiting the statment new fork()')
            if reply == 'c':
                continue
            else:
                break
parent()