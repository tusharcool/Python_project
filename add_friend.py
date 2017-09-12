from globals import friends

def add_friend():

    new_friend={'name':" ",
                'salutation':".",
                'age': 0,
                'rating': 0.0,
                'status': False
    }

    new_name=raw_input("Please add your friend")
    new_salutation=raw_input("Enter the salutation")
    new_name=new_salutation+"  "+new_name
    new_rating=float(raw_input("Spy Rating?"))
    new_age=int(raw_input("Age?"))

    # proper validation by the user
    if len(new_name)>0 and new_age >12 and new_age <50 and len(new_rating)>0:
        #add friend
        friends.Append(new_friend)
        print 'Friend Added'
    else:
        print "invalid entry"

    return len(friends)