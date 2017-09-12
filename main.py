from spy_details import spy
from start_chat import start_chat


print 'Let\'s get started'
question='Do you want to continue as'+spy['salutation']+"  "+spy['name']+ ' (y/n)  '
existing=raw_input(question)
# check validating user input
if (existing=='Y' or existing=='y'):
    spy['name']=spy['salutation']+"  "+spy['name']
    start_chat(spy['name'],spy['age'],spy['rating'],spy['is_online']);

elif (existing=='N' or existing =='n'):
    #new users code
    spy['name'] = raw_input("what is ur name ?")
    if len(spy['name']) > 0:
        if spy['name'].isalpha():
            print "Alright" + spy['name'] + " I would like to know better before to proceed further.."
            spy['salutation'] = raw_input('what is ur salutaion')
            spy['name'] = spy['salutation'] + " " + spy['name']
            print 'welcome ' + spy['name'] + ' glad to here with you'
            spy['age'] = 0
            spy['rating'] = 0.0
            spy['online'] = False
            print type(spy['age'])
            spy['age'] = int(raw_input('Enter the age of spy '))
            if (type(spy['age']) == int):
                print 'valid age'
            if spy['age'] > 15 and spy['age'] < 50:
                spy['rating'] = bool(raw_input("enter the rating"))
                print type(spy['rating'])
            else:
                "not valid age"
        else:
            print"INVALID name"
    # concatination of salutation and name.


    else:
        print 'Not valid in'
else:
    print "wrong choice try again"
