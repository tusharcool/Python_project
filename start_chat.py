# start chat function definition

def start_chat(name,age,rating):
    show_menu=True
    while show_menu:
        menu_choices="what do u want to do ? \n 1. Add status \n 2.close application"
        result =int(raw_input(menu_choices))
        # validationg users input
        if (result==1):
            # action
            pass
        elif(result==2):
            show_menu=False
        else :
            print "wrong choices"
