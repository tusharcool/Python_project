from globals import friends
from spy_details import spy
import re

spy = spy('Tushar', 'Mr.', 34, 6.0)
class add_friend:

    def __init__(self,name,salutation,age,rating):
        self.name=name
        self.salutation=salutation
        self.age=age
        self.rating=rating
        self.chats = []


    def new_friend(self):

        temp = True  # temporary variable

        patternsalutation = '^Mr.|Ms.$'
        patternname = '^[A-Za-z][A-Za-z\s]+$'
        patternage = '^[0-9]+$'
        patternrating = '^[0-9]+\.[0-9]$'
        # Validating Each Values Using Regular Expression
        while temp:
            salutation = raw_input("Mr. or Ms.? : ")
            if (re.match(patternsalutation, salutation) != None):
                temp = False
            else:
                print ("Enter Again!!!!")
        temp = True
        while temp:
            name = raw_input("Enter Name: ")
            if (re.match(patternname, name) != None):
                temp = False
            else:
                print ("Enter Again!!!!")
            name = salutation + "." + name
        temp = True
        while temp:
            age = raw_input("Age?")
            if (re.match(patternage, age) != None):
                temp = False
                age = int(age)
            else:
                    print ("Enter Again!!!!")
        temp = True  # temporary variable
        while temp:
             rating = raw_input("Spy rating?")
             if(re.match(patternrating, rating) != None):
                temp = False
                rating = float(rating)
             else:
                 print ("Enter Again!!!!")

        # proper validation by the user
        addfriend = add_friend(name, salutation, age, rating)

        if len(addfriend.name)>0 and addfriend.age >12 and addfriend.rating>=spy.rating:
                #add friend
            friends.append(addfriend)
            print 'Friend Added'
        else:
            print "invalid entry"

        return len(friends)