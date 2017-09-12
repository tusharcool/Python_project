from globals import friends

def select_friend():
    count=0
    for friend in friends:
        print "%d %s" %(count+1),friend['name']
        conu=count+1

    friend_choice = raw_input("choose your friend")
    friend_choice_position=int(friend_choice)-1
    return friend_choice_position

x=select_friend
print x