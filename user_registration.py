# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
def registration() :
    name =""
    key =""
    mail =""
    def user_name() :
        nonlocal name
        name = input("Enter your user name : ").title()
        control(name = name)
    def control(name ="", mail="") :
        for i in open("users.txt", "r", encoding = "utf-8",).readlines() :
            check = i.split()
            if check[1] == name :
                print("-" * 70)
                print(f"{name} has been already used, please enter another user name")
                print("-" * 70)
                return user_name()
            if check[5] == mail :
                print("-" * 70)
                print(f"{mail} has been already used, please enter with your e-mail addres")
                print("-" * 70)
                return email()
    def password() :
        nonlocal key
        key = input("Please enter your password : ")
        key_r = input("Please enter your password again : ")
        if key != key_r :
            print("-" * 70)
            print("Passwords are not same please enter your paswords again!")
            print("-" * 70)
            return password()
    def email() :
        nonlocal mail
        mail = input("Please enter your e-mail address : ").lower()
        mail2 = input("Please enter your e-mail address again : ").lower()
        if mail != mail2 :
            print("-" * 70)
            print("-" * 70)
            print("E-mail adress are not same, please enter your e mail address again!")
            return email()
        else : return control(mail = mail)
    email()
    user_name()
    password()
    with open("users.txt", "a", encoding = "utf-8") as users :
        users.write("user_name ")
        users.write(name)
        users.write(" password ")
        users.write(key)
        users.write(" e-mail ")
        users.write(mail)
        users.write("\n")
    print("-" * 70)
    print("User was successfully registered")
    print("-" * 70)

online = False

def entrance() :
    name = ""
    key = ""
    name = input("Pleaase enter your user name : ").title()
    key = input("Please enter your password : ")
    for i in open("users.txt", "r", encoding = "utf-8").readlines():
        check = i.split()
        if check[1] == name and check[3] == key :
            print(f"Welcome {name}")
            global online
            online = name
            break
    else:
        print("-" * 70)
        print("User name or password are invalid, please try again!")
        print("-" * 70)
        return entrance()
if __name__ == "__main__" : 
    while True :     
        print( """

        Please choose one of process below :

        [1] Registration
        [2] Entrance

        """)
        num =""
        try : 
            num = int(input("Please enter your choise as number : ").strip())
            while num not in [1, 2] :
                try :
                    num = int(input("It was invalid entrance, Please enter your choise as 1 or 2 :").strip())
                except :
                    num = 10
        except :
            while num not in [1, 2] :
                try :
                    num = int(input("It was invalid entrance, Please enter your choise as 1 or 2 :").strip())
                except :
                    num = 10 
        if num == 1 :
            registration()
        elif num == 2 :
            entrance()
        break


# %%



# %%



# %%



# %%



# %%



# %%



# %%



