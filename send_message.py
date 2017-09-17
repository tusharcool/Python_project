from select_a_friend import select_friend
from steganography.steganography import Steganography
from datetime import datetime
from ChatMessage import ChatMessage
from globals import friends
from spy_details import spy
from add_friend import add_friend
import re

add = add_friend("","",0,0.0)
chats = add.chats

def send_message():

     #chose a friend from a list.

     friend_choice = select_friend()

     pattern = '\w+\.(jpg|gif|png)'  # Regex for correct name pattern for image
     a = True  # Temporary Variable
     # prepare the  message

     while a:
          original_image = raw_input("Provide the name of the image to hide the message: ")
          if (re.match(pattern, original_image) != None):
               a = False
          else:
               print ("Enter Again!!!!")
     a = True
     while a:
          output_image = raw_input("Provide the name of the output image : ")
          if (re.match(pattern, output_image) != None):
               a = False

     text = raw_input("Enter your message here: ")
     if (len(text) > 100):
          # remove friend he/she types more 100 words
          print ("Large Message Input!!!!")
          print ("You are no more a Spy!!!!")
          friends.remove(friends[friend_choice])
     else:
          # Handling Exception If Image Does Not Exist
          try:
               # Encrypt the message
               Steganography.encode(original_image, output_image, text)
               new_chat = ChatMessage(text, True)
               friends[friend_choice].chats.append(new_chat)

               # Successful message
               print ("Your message encrpyted successfully")
               # Handling Situation For SOS|Danger
               if ( text.upper()=="SOS" or text.upper()=="SAVE ME" or text.upper()=="IN DANGER"):
                    print ("I got your location!!!!I'll be there soon!")
          except IOError:
               print ("Image %s Does Not Exist!!!!" % (original_image))
