from spy_details import spy
from start_chat import start_chat
import re


spy =spy('Tushar','Mr.',34,6.0)
print 'Let\'s get started'
question='Do you want to continue as'+spy.salutation+"  "+spy.name+ ' (y/n)  '
existing=raw_input(question)
# check validating user input
if (existing=='Y' or existing=='y'):
    spy.name=spy.salutation+"  "+spy.name
    start_chat(spy.name,spy.age,spy.rating,spy.is_online)

elif (existing=='N' or existing =='n'):
    #new users code
    temp = True  # temporary variable

    patternsalutation = '^Mr|Ms$'
    patternname = '^[A-Za-z][A-Za-z\s]+$'
    patternage = '^[0-9]+$'
    patternrating = '^[0-9]+\.[0-9]$'
    # Validating Each Values Using Regular Expression
    while temp:
        salutation = raw_input("Mr. or Ms.? : ")
        if (re.match(patternsalutation, salutation) != None):
            tempcheck = False
        else:
            print("Enter Again!!!!")
    temp = True
    while temp:
        spy.name = raw_input("Enter Name: ")
        if (re.match(patternname, spy.name) != None):
            temp = False
        else:
            print("Enter Again!!!!")
    # concatenation.
    spy.name = salutation + "." + spy.name
    temp = True
    while temp:
        spy.age = raw_input("Age?")
        if (re.match(patternage, spy.age) != None):
            temp = False
            spy.age = int(spy.age)
        else:
            print ("Enter Again!!!!")
    temp = True
    while temp:
        spy.rating = raw_input("Spy rating?")
        if (re.match(patternrating, spy.rating) != None):
            temp = False
            spy.rating = float(spy.rating)
        else:
            print ("Enter Again!!!!")

    # concatination of salutation and name.
else:
    print "wrong choice try again"
