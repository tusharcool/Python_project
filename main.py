from spy_details import spy
from start_chat import start_chat


print 'Let\'s get started'
question='Do you want to continue as'+spy['Salutation']+"  "+spy['Name']+ ' (y/n)  '
existing=raw_input(question)
# check validating user input
if (existing=='Y' or existing=='y'):
    start_chat(spy_name,spy_age,spy_rating)
    pass
elif (existing=='N' or existing =='n'):
    #new users code
    spy_name = raw_input("what is ur name ?")
    if len(spy_name) > 0:
        if spy_name.isalpha():
            print "Alright" + spy_name + " I would like to know better before to proceed further.."
            spy_salutation = raw_input('what is ur salutaion')
            spy_name = spy_salutation + " " + spy_name
            print 'welcome ' + spy_name + ' glad to here with you'
            spy_age = 0
            spy_rating = 0.0
            spy_online = False
            print type(spy_age)
            spy_age = int(raw_input('Enter the age of spy '))
            if (type(spy_age) == int):
                print 'valid age'
            if spy_age > 15 and spy_age < 50:
                spy_rating = bool(raw_input("enter the rating"))
                print type(spy_rating)
            else:
                "not valid age"
        else:
            print"INVALID NAME"
    # concatination of salutation and name.


    else:
        print 'Not valid in'
else:
    print "wrong choice try again"
