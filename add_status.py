def add_status(status_message):
    STATUS_MESSAGES=[]
    # logic.
    if (status_message != None):
        print"your status is"+ status_message+"\n"
    else:
        print "no status \n"
    default = raw_input("do you want to select older messages (y/n)?")

    if default.upper()=='N':
        new_status_message = raw_input("what status message do you want to set?")

        if len(new_status_message)>0:
            updated_status_meaasge = new_status_message
            STATUS_MESSAGES.aapend(updated_status_meaasge)

    elif default.upper()=='Y':
        item_position=1
        for message in STATUS_MESSAGES:
            print item_position+" "+message
            item_position=item_position+1
        message_selection = int(raw_input("\n choose from above message"))
        if len(STATUS_MESSAGES)>=message_selection:
            updated_status_meaasge = STATUS_MESSAGES[message_selection-1]

    return updated_status_meaasge
