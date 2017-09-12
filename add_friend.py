from globals import friends
from spy_details import spy

def add_friend():

    new_friend={'name':" ",
                'salutation':".",
                'age': 0,
                'rating': 0.0,
                'status': False
    }

    new_friend['name']=raw_input("Please add your friend")
    new_friend['salutation']=raw_input("Enter the salutation")
    new_friend['name']=new_friend['salutation']+"  "+new_friend['name']
    new_friend['rating']=float(raw_input("Spy Rating?"))
    new_friend['age']=int(raw_input("Age?"))

    # proper validation by the user
    if len(new_friend['name'])>0 and new_friend['age'] >12 and new_friend['rating']>=spy['rating']:
        #add friend
        friends.append(new_friend)
        print 'Friend Added'
    else:
        print "invalid entry"

    return len(friends)