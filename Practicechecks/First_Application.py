import urllib
import os
import colorama
from datetime import datetime
from colorama import Fore, Back, Style
import time
print "My second Program!"
try :
    curDir=os.getcwd()
    current_time=datetime.today()
    print ('Current time is '+str(current_time))
    print ('Current Directory:'+curDir)
    i = 0
    linenumber = 0
    othercode=""
    ifdefchar=""
    define_list=list()
    terminate=""
    definestatment=""
    definervalue=list()
    definer=list()
    main_file=open('Compiled1.cpp','w')
    check=bool(raw_input("Do you want to check the  message system ithrough Shafay's Compiler!?"))
    if check is True:
        print ("ALL RIGHT RESERVED TO MUHAMMAD SHAFAY AMJAD 454-BSCS-13 PythonWorkspace")
        FILE=open('DATA.cpp','r')
        Message_recieved=FILE.readlines()
        for M in Message_recieved:
            linenumber=linenumber+1  # to keep the Track of line number in the code to predict errors
            #print (M[i])
            while M[i] is ' ':
                i=i+1
            if M[i] is '#':
                i = i + 1
                if M[i] is 'i':
                    i = i + 1
                    if M[i] is 'n':
                        i = i + 1
                        if M[i] is 'c':
                            i = i + 1
                            if M[i] is 'l':
                                i= i + 1
                                if M[i] is 'u':
                                    i = i + 1
                                    if M[i] is 'd':
                                        i = i + 1
                                        if M[i] is 'e':
                                            print ("There is an include library in it :)")
                                            i = i + 1
                                            if M[i] is '<' or M[i] is '"':
                                                end = M[i]
                                                #j = 0
                                                i = i + 1
                                                char=list()
                                                if end is '<':
                                                    terminate='>'
                                                elif end is '\"':
                                                    terminate='\"'
                                                else:
                                                    print ("there is an error in the line "+str(linenumber)+'/n TIme is '+str(current_time))
                                                    break
                                                while M[i] != terminate:
                                                    char.append(M[i])
                                                    i = i + 1
                                                print ('The library is '+str(char))
                                                headerfile_name=""
                                                i=i+1
                                                for k in char:
                                                    headerfile_name=headerfile_name + str(k)
                                                print headerfile_name
                                                if headerfile_name == "iostream":
                                                    print ("Including the header file iostream")
                                                    headerfile1=open('C:\\Program Files (x86)\\CodeBlocks\\MinGW\\lib\\gcc\\mingw32\\4.7.1\\include\\c++\\iostream','r') #Reading the header file here!
                                                    headerfile1data=headerfile1.readlines()
                                                    for line in headerfile1data:
                                                        main_file.write(line+'\n')
                                                elif headerfile_name=="conio.h":
                                                    print("Including Conio.h header File")
                                                    headerfile2=open('C:\\Program Files (x86)\\CodeBlocks\\MinGW\\include\\conio.h','r') #reading form the second header FIle!.
                                                    headerfile2data=headerfile2.readlines()
                                                    for line in headerfile2data:
                                                        main_file.writelines(line)
                                                elif headerfile_name=="io.h":
                                                    print("including another header file IO")
                                                    path="C:\\Program Files (x86)\\CodeBlocks\\MinGW\\lib\\gcc"
                                                    headerfile3=open(path+'\\mingw32\\4.7.1\\include\\c++\\mingw32\\bits\\c++io.h','r') # for including the header file 3 path
                                                    headerfile3data=headerfile3.readlines()
                                                    for line in headerfile3data:
                                                        main_file.write(line+'\n')
                                                elif headerfile_name=="stdlib":
                                                    print ("includding another header file to the directory")
                                                    path="C:\Program Files (x86)\CodeBlocks\MinGW\include\stdlib.h"
                                                    headerfile4=open(path,'r')
                                                    headerfile4data=headerfile4.readlines()
                                                    for line in headerfile4data:
                                                        main_file.write(line)
                                                i = 0

                                            else:
                                                print ('###There is an error in the header File at: '+str(linenumber)+' \n TIme is '+str(current_time))
                                                break
                                                i = 0
                                        else:
                                            print ('###There is an error in the header File at : '+str(linenumber)+'\n TIme is '+str(current_time))
                                            break
                                            i=0
                                    else:
                                        print ('###There is an error in the header File at#### '+str(linenumber)+'\n TIme is '+str(current_time))
                                        break
                                        i=0
                                else:
                                    print ('###There is an error in the header File at#### '+str(linenumber)+'\n TIme is '+str(current_time))
                                    break
                                    i=0
                            else:
                                print ('###There is an error in the header File at#### '+str(linenumber)+'\n TIme is '+str(current_time))
                                break
                                i=0
                        else:
                                print ('###There is an error in the header File at#### '+str(linenumber)+'\n TIme is '+str(current_time))
                                break
                                i=0
                    #probelm is here somewhere the defination is wrong
                    elif M[i]=='f':
                         #Write the MainFile COde here
                        i=i + 1
                        if M[i]=='d':
                            i = i + 1
                            if M[i]=='e':
                                i = i + 1
                                if M[i]=='f':
                                    i = i + 1
                                    if M[i] is ' ':
                                        i = i + 1
                                        ifdefchar+=M[i]
                                        i = i + 1
                                        #while M[i] != ' ':
                                         #   ifdefchar+=M[i]
                                          #  i = i + 1
                                        main_file('IFDEF HERE-->')
                                    if ifdefchar in define_list:
                                        print ('defined preprocesser')
                                        # # ### You are Writing code here!
                                    else:
                                        print ('Non Defined preprocessor'+'Error at line '+str(linenumber)+'\nChecked at:'+str(current_time))
                        elif M[i]==' ':
                            print ('There is an if defination in this place!')

                        i = i + 1
                elif M[i]=='#':
                    Error_generator='There is an error in the code ## at line'
                    # To keep he Track of code error write Line here
                    print (Fore.RED,Error_generator)
                    print ('On LINE NUMBER: '+str(linenumber)+'/n TIme is '+str(current_time))
                    #print 'There is an error in the code ## at line'+str(linenumber)
                    break

                elif M[i]=='e':
                    i = i + 1
                    if M[i] =='r':
                        i = i + 1
                        if M[i]=='r':
                            i= i + 1
                            if M[i]=='o':
                                i = i + 1
                                if M[i]=='r':
                                    i = i + 1
                                    if M[i]==' ':
                                        i = i + 1
                                        print '---> There is an error defination here****!!' # Write the detail of the Error File.
                                        if M[i]== '"':
                                           ''' main_file.write("cout<<") # defining the statment of the error defination
                                            i = i + 1
                                            main_file.write("\"")
                                            while M[i] is not '"':
                                                main_file.write(M[i])
                                                i = i + 1
                                            main_file.write(M[i])
                                            main_file.write(';')  # Terminating the error statment
                                        #Write the ERROR Duirectory Code here!

                                        '''
                elif M[i]=='d':
                    i = i + 1
                    if M[i]=='e':
                        i = i + 1
                        if M[i]=='f':
                            i = i + 1
                            if M[i]=='i':
                                i = i +1
                                if M[i]=='n':
                                    i= i + 1
                                    if M[i]=='e':
                                        i = i + 1 #define file needed to be handle
                                        while M [i] is ' ':
                                            i = i + 1  # FOr excluding the spaces before the defineative variable
                                        while M[i] is not ' ':
                                            definer.append(M[i]) #to append the definative variable
                                            i = i + 1
                                        while M[i] is ' ':
                                            i = i + 1            #to eliminate extra spacess
                                        define_list.append(definer)
                                        if M[i]=='\"':
                                            i = i + 1
                                            while M[i] is not '\"':
                                                definervalue.append(M[i])
                                                i = i + 1
                                        else:
                                            print ("Error at line "+str(linenumber)+" checked on time "+str(current_time))
                                            break
                                        main_file.write('Global'+str(definer)+'='+str(definervalue))
                                        i = 0  #Write the statment to handle multiple
            elif M[i] is not '#' and M[i] is not '{' and M[i] is not 'r' and M[i] is not '}':
                othercode=""
                try:
                    while M[i] is ' ':
                        i = i + 1
                    while M[i] is not '\n' and ' ':
                        othercode = othercode+ str(M[i])
                        i=i+1
                        if othercode == "int main()":
                            print ("int main()")
                            main_file.write("int main()")
                            i=0
                            break
                        else:
                            continue
                            #i=i+1
                    i=0
                except ValueError:
                    print ("THere is an error atthe line"+linenumber+'\n at time'+current_time)
            elif M[i] is '{' or M[i] is 'r' :
                additionalcode=""
                while M[i] is ' ':
                    i = i + 1
                while M[i] is not '\n':
                    additionalcode += M[i]
                    if M[i] is not ';':
                        i=i+1
                    elif M[i] is ';':
                        i=i+1
                        break
                    elif M[i] is '}':
                        print M[i]
                        break
                print (additionalcode)
                main_file.write(additionalcode)
            else:
                print ("There is an error at "+str(linenumber))
            i=0
        main_file.write('}')
        print ('}')
       # print(Message_recieved)
except ValueError:
    print("There is an error in the code at line "+linenumber+'\n TIme is '+str(current_time))#"An error occured :" +ValueError+ "at line "+linenumber)
