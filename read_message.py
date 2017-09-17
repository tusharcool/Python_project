from select_a_friend import select_friend
from steganography.steganography import Steganography
from ChatMessage import ChatMessage
from globals import friends
from add_friend import add_friend

add = add_friend("","",0,0.0)
chats = add.chats

count = 0
def read_message():
    global count
    sender = select_friend()

    output_path = raw_input("Enter the output image:-")
    received_txt = Steganography.decode(output_path)

    new_chat = ChatMessage(received_txt,False)
    friends[sender].chats.append(new_chat)

    print "Your scret message has been saved"

    avg=0
    for chat in friends[sender].chats:
        avg = avg + len(chat.message)
        avg = avg/(count+1)

    print "avg word spoken ", avg