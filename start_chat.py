# start chat function definition
from add_status import add_status
from add_friend import add_friend
from send_message import send_message
from add_status import add_status
from spy_details import spy
from read_message import read_message
from read_chat_history import  read_chat_history

addfriend = add_friend("","",0,0.0)

def start_chat(name,age,rating,status):
    from globals import current_status_message

    error_message=None

    if not (age>12 and age<50):
        error_message=""
        print error_message
    else:
        welcome_message="Authentication done welcome \n"\
                "Name:"+name+"\n"\
                "Age:"+str(age)+"\n"\
                "Rating"+str(rating)+"\nis_online"+str(status)
        print welcome_message
        show_menu=True
        while show_menu:
            menu_choices="what do u want to do ? \n"\
                    "1. Add status update \n"\
                    "2 Add a Friend \n"\
                    "3. Send a secret message \n"\
                    "4. Read a secret message \n"\
                    "5. Read chat from a user \n"\
                    "6. exit application \n"
            result =int(raw_input(menu_choices))
            # validationg users input
            if (result==1):
                 current_status_message= add_status(current_status_message)
            elif(result==2):
                number_of_friends=addfriend.new_friend()
                print "you have %d friends"% number_of_friends
            elif(result==3):
                send_message()
            elif(result==4):
                read_message()
            elif(result==5):
                read_chat_history()
            elif(result==6):
                show_menu=False
            else :
                print "wrong choices"
