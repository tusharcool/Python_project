from select_a_friend import select_friend
from steganography.steganography import Steganography
from datetime import datetime
from ChatMessage import ChatMessage
from globals import friends

def send_message():

     #chose a friend from a list.

     friend_choice = select_friend()

     original_image =raw_input("what is the name of the image?")
     output_image = raw_input("provide the name of output image:-")
     text = raw_input("what do u want to say?")
     Steganography.encode(original_image,output_image,text)

     new_chat = ChatMessage(text,True)

     friends[friend_choice].chats.append(new_chat)

    print "Your msg encrypted successfully."
