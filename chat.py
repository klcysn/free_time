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

def personal_menu(name, choise = "") : # name user_registration.online'dan geliyor
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
                choise = 10 #en son except'de hata vermemesi için

        if choise == 1 :
            friend_list()

        elif choise == 2 :
            friend = input("Please enter your friend's name : ").title()
            add_friends(name = name, friend = friend) #sözlük olarak fonksiyona yolluyoruz.
 
        elif choise == 3 :
            friend = input("Please enter your friend's name you want to send message : ").title()
            for i in open("friends.txt", "r", encoding="utf-8").readlines() :
                lst = i.split() # isimlere liste şeklinde ulaşmak için ["name", "friend"]
                if lst[0] == name and friend == lst[1] : #friend'in arkadaş listemizde olup olmadığını kontrol ediyor.
                    msg = input("Enter your message here : ")
                    msg_snd(name = name, friend = friend, message = msg, date = datetime.now())
                    break # burada break yapmazsan else'i de okutur.
            else : #eğer yoksa tekrar gönderiyor friend ismi girmeye
                print(f"{friend} was not found in your friend's list")
                personal_menu(name, choise = 3)

        elif choise == 4 :
            msg_box(name)

        elif choise == 5 :
            ext(name)

        break # yapmazsak menüyü sonsuz olarak her işlem bittiğinde tekrar açar
        
def add_friends(**data) : #sınırsız sözlük değeri alması için
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
    friend_stiuation = True # eğer arkadaş yoksa aşağıda if'i print yapmak için
    for i in open("friends.txt", "r", encoding="utf-8").readlines() :
        lst = i.split() # isimlere liste şeklinde ulaşmak için ["name", "friend"]
        if lst[0] == user_registration.online :
            print(lst[1])
            friend_stiuation = False
    if friend_stiuation : print("You haven't had any friend yet.") #arkadaş yoksa burası çalışacak
    answr = input("Would you like to go back menu(Y/N) :  ").capitalize()
    if answr == "Y" : personal_menu(user_registration.online)
    else : pass


def msg_snd(**data) :
    friend = data["friend"] # printin içinde kullanmak için aksi halde hata veriyor
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
            input("To continue press enter!") # print'i okuyana kadar bekletir daha sonra bir tuşa basınca altındaki işleme geçer 
            personal_menu(name = name, choise = "")


    elif choise_box == 2 :
        for i in open("message.txt", "r", encoding="utf-8").readlines() :
            box = i.split()
            if box[0] == name :
                print(f"Sent to {box[1]} ---> {' '.join(box[2:len(box) -2])} <---- in {' '.join(box[len(box) - 2:])}")
                print("-" * 80)
#' '.join(iterable) yapmazsan slice yaptığın değerleri liste içinde virgülle ayırarak veriyor. Tek tırnak olmasına dikkat et.
# eğer mesajı yazdırırken varable'lar arasına boşluk yerine başka karater koysaydık "-" gibi spliti buradan yapardık ve join kullanmamıza gerek kalmazdı ve mesaj 4 değere böünmüş olurdu. Ama mesaj içerisinde geçmeyecek bir karakter olması gerekli örn;"||" gibi
        else :
            print("-" * 70)
            print("You have read all message!")
            print("-" * 70)
            input("To continue press enter!") # print'i okuyana kadar bekletir daha sonra bir tuşa basınca altındaki işleme geçer 
            personal_menu(name = name, choise = "")


def ext(name) :
    print("-" * 70)
    print(f"You exit succesfully!\nWe would like to see you again\nGood Bye {name}")
    print("-" * 70)
    user_registration.online = False
    pass


if __name__ == "__main__" : # eğer script direkt çalıştırılıyorsa burası çalışır

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
                    num = 10 # ne kadar except yazsanızda en son excepte numeric olmama hatası verir
        if num == 1 :
            user_registration.registration()
        elif num == 2 :
            user_registration.entrance()
            personal_menu(user_registration.online)

        break


# %%



