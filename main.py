print 'Let\'s get started'
spy_name = raw_input("what is ur name ?")
if  len(spy_name)>0:
    print "Alright" + spy_name +" I would like to know better before to proceed further.."
    spy_salutation = raw_input('what is ur salutaion')
# concatination of salutation and name.
    spy_name = spy_salutation + " " + spy_name
    print 'welcome ' + spy_name + ' glad to here with you'
else :
    print 'Not valid input'