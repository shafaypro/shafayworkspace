import sys
print(sys.version)  # gives the version of the machine.
inputstatment = sys.stdin.readline()
print(inputstatment)
# you can take the first 10 character or the last t10 depending upon what result you want.
readline = sys.stdin.readline(10)
print(readline)  # everything after the first 10 character is skipped.
sys.stdout.write("This is the awesomistic statmetn")  # This is the ouput on the console
