def add_friend():
    friend_name=[]
    friend_age=[]
    friend_rating=[]
    friend_status=[]

    new_name=raw_input("")
    new_salutation=raw_input("")
    new_name=new_salutation+"  "+new_name
    new_rating=raw_input("")
    new_age=raw_input("")

    new_age=int(new_age)
    new_rating=float(new_rating)
    if len(new_name)>0 and new_age >12 and new_age <50 and len(new_rating)>0:
        #add friend
        friend_name.append(new_name)
        friend_age.append(new_age)
        friend_rating.append(new_rating)
        friend_status.append(True)
    else:
        print "invalid entry"

    return len(friend_name)