# Given a list of numbers and a number k, return whether any two numbers from the list add up to k. For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

x = input("Please enter your list with comma without space : ")

lst = x.split(",")

k = int(input("Please enter your total number : "))

for i in lst :
    for j in lst:
        if i == j :
            continue
        else :
            if int(i) + int(j) == k :
                print(i, "+", j, "=", k)
            break