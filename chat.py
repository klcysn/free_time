# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
""" Please before run script, create an "users.txt" in folder is this script in.

This script register users,
show your friends you added,
add your friends,
send message to your friends,
show message came to you""" 

import user_registration
from datetime import datetime

def personal_menu(name, choise = "") : # name came from user_registration.online
    while name :
        if choise == "" :
            print(f"{name}'s Menu !")
            print("""

            [1] Friends List
            [2] Add Friends
            [3] Send Message
            [4] Message Box
            [5] Quit

            Please enter your choise as number : 
            
            """)
        while choise not in [1, 2, 3, 4, 5] :
            try :
                choise = int(input("Please enter  from 1 or 5 : "))
                break
            except :
                print("Invalid value!, Please enter from 1 or 5 : ")
                choise = 10 #to not give error at last except

        if choise == 1 :
            friend_list()

        elif choise == 2 :
            friend = input("Please enter your friend's name : ").title()
            add_friends(name = name, friend = friend) #we send it as dictionary.
 
        elif choise == 3 :
            friend = input("Please enter your friend's name you want to send message : ").title()
            for i in open("friends.txt", "r", encoding="utf-8").readlines() :
                lst = i.split() #  to make line list ["name", "friend"]
                if lst[0] == name and friend == lst[1] : #it checks friend is in our friend list or not.
                    msg = input("Enter your message here : ")
                    msg_snd(name = name, friend = friend, message = msg, date = datetime.now())
                    break # it read also else without break.
            else : #if we don't put this, it asks friend again
                print(f"{friend} was not found in your friend's list")
                personal_menu(name, choise = 3)

        elif choise == 4 :
            msg_box(name)

        elif choise == 5 :
            ext(name)

        break # it open personal menu after every function without break
        
def add_friends(**data) : #to take endless input
    with open("friends.txt", "a", encoding="utf-8") as frnd :
        frnd.write(data["name"])
        frnd.write(" ")
        frnd.write(data["friend"])
        frnd.write("\n")
    print("Your friends was added in friends list")
    answr = input("Would you like to add another friend (Y/N) : ").capitalize()
    if answr == "Y" :
        friend = input("Please enter your friend's name : ")
        add_friends(name = user_registration.online, friend = friend)
    elif answr == "N" :
        personal_menu(user_registration.online)


def friend_list() :
    friend_stiuation = True # if there is no friend, it run if code is below
    for i in open("friends.txt", "r", encoding="utf-8").readlines() :
        lst = i.split() # to make line list ["name", "friend"]
        if lst[0] == user_registration.online :
            print(lst[1])
            friend_stiuation = False
    if friend_stiuation : print("You haven't had any friend yet.") #if there is no friend, here runs
    answr = input("Would you like to go back menu(Y/N) :  ").capitalize()
    if answr == "Y" : personal_menu(user_registration.online)
    else : pass


def msg_snd(**data) :
    friend = data["friend"] # to  use in print otherwise it gives error
    with open("message.txt", "a", encoding="utf-8") as m :
        m.write(data["name"])
        m.write(" ")
        m.write(data["friend"])
        m.write(" ")
        m.write(data["message"])
        m.write(" ")
        m.write(str(data["date"]))
        m.write("\n")
    print(f"Message was sent to {friend}")
    personal_menu(name = name, choise = "")


def msg_box(name) :
    print("""
    Would you like to see message;
    [1] You Received
    [2] You sent""")
    choise_box = ""
    while choise_box not in [1, 2] :
        try :
            choise_box = int(input("Please enter your choise as number : "))
        except :
            choise_box = int(input("Invalid value, Please enter your choise as number : "))
            choise_box = 10

    if choise_box == 1 :
        for i in open("message.txt", "r", encoding="utf-8").readlines() :
            box = i.split()
            if box[1] == name :
                print(f"From {box[0]} ---> {' '.join(box[2:len(box) -2])} <---- in {' '.join(box[len(box) - 2:])}")
                print("-" * 80)
        else :
            print("You have read all message!")
            input("To continue press enter!") # it makes you wait until press enter 
            personal_menu(name = name, choise = "")


    elif choise_box == 2 :
        for i in open("message.txt", "r", encoding="utf-8").readlines() :
            box = i.split()
            if box[0] == name :
                print(f"Sent to {box[1]} ---> {' '.join(box[2:len(box) -2])} <---- in {' '.join(box[len(box) - 2:])}")
                print("-" * 80)
#' '.join(iterable) helps you to print text, not list
# if we wrote with symbol like "||" in message.txt, we wouldn't have to use slice, and ' '.join()
        else :
            print("-" * 70)
            print("You have read all message!")
            print("-" * 70)
            input("To continue press enter!") # it makes you wait until press enter  
            personal_menu(name = name, choise = "")


def ext(name) :
    print("-" * 70)
    print(f"You exit succesfully!\nWe would like to see you again\nGood Bye {name}")
    print("-" * 70)
    user_registration.online = False
    pass


if __name__ == "__main__" : #if script runs directly, here runs first 

    while True :
        print("""
        
        Please enter your choise as number in the box :

        [1] Registration
        [2] Entrance
        
        """)
        num =""
        try :
            num = int(input("Please enter 1 or 2 : "))
            while num not in [1, 2] :
                try :
                    num = int(input("Invalid value!, Please enter 1 or 2 :  "))
                except :
                    print("Invalid value!, Please enter 1 or 2 : ")
                    num = 10
        except :
           while num not in [1, 2] :
                try :
                    num = int(input("It was invalid entrance, Please enter your choise as 1 or 2 :").strip())
                except :
                    num = 10 #  to not give error at last except
        if num == 1 :
            user_registration.registration()
        elif num == 2 :
            user_registration.entrance()
            personal_menu(user_registration.online)

        break


# %%



