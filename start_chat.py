# start chat function definition
from add_status import add_status


def start_chat(name,age,rating):
    show_menu=True
    while show_menu:
        menu_choices="what do u want to do ? \n 1. Add status \n 2.close application"
        result =int(raw_input(menu_choices))
        # validationg users input
        if (result==1):
            current_status_message= add_status(current_status_message)
        elif(result==2):
            show_menu=False
        else :
            print "wrong choices"
