from select_a_friend import select_friend
from steganography.steganography import Steganography
from ChatMessage import ChatMessage
from globals import friends

def read_message():
    sender = select_friend()

    output_path = raw_input("Enter the output image:-")
    received_txt = Steganography.decode(output_path)

    new_chat = ChatMessage(received_txt,False)
    friends[sender].chats.append(new_chat)

    print "Your scret message has been saved"