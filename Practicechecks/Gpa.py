checker=True  # just tp check the condition rather to be true of false
counter=1     # To keep track of the current Semester
TOTAL_CGPA=0.0; #count the total cgpa variable
checker = raw_input('Do you want to continue and False to Cancel now')
while(checker == 'True'):
    GPA=  '''Here write the function called having a return type which you had made before '''
    TOTAL_CGPA += GPA
    checker = raw_input('Add Another Semester? True to continue , False to finish')
    counter += 1
print ('Your Cgpa Till now is :',TOTAL_CGPA/(counter-1))

