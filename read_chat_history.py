from colorama import *
from select_a_friend import select_friend
from globals import friends
from add_friend import add_friend
from ChatMessage import ChatMessage

add = add_friend("","",0,0.0)
chats = add.chats

CM = ChatMessage("","")
sent_by_me = CM.sent_by_me
message = CM.message


def read_chat_history():
    read_for = select_friend()

    print'\n'

    for chat in friends[read_for].chats:
        if chat.sent_by_me == True:
            print "[%s]%s:%s"%(Fore.BLUE+chat.time.strftime("%d %B %Y"),'You said:',Fore.BLACK+chat.message)
            break
        else:
            print "[%s]%s:%s" % (Fore.BLUE+chat.time.strftime("%d %B %Y"), Fore.RED+friends[read_for].name, Fore.BLACK+chat.message)
            break
