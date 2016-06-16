import parser

def parsetreechecker(F_expressioncomplete):
    print ('In the function')
    print ('The expression you entered is '+str(F_expressioncomplete))
    line=F_expressioncomplete.split('(')
    print line[0]
    line_generated=line[1].split(')')
    i = 0
    for i in line_generated:
        line_generatedwithin=i
        line_generatedwithin=line_generatedwithin.split(';')
        for finalsplit in line_generatedwithin:
            print finalsplit


def experessionchecker():
    print ('Expression checker class')



print('Start Writing the main program here!')
expressioncomplete = raw_input('Enter the expression to be parsed !') #Taking the expression input
print ('The expression you entered is !!!:'+str(expressioncomplete))
parsetreechecker(expressioncomplete) #passing to the expression function!
pa=parser.expr('9+2')
print(pa)


