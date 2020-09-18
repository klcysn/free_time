prefix = input("please enter your prefix : ")
string_set = input("Please enter string set with comma and without space : ")

lst = string_set.split(",")
lst_2 = [i for i in lst if i.startswith(prefix)]

lst_2