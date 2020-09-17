# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well. For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

x = input("Please enter your array without space and with comma : ")
lst = x.split(",")
lst_num = []
for i in lst :
    lst_num.append(int(i))

for i in range(1, max(lst_num)) :
    if i in lst_num :
        continue
    else :
        print(i)
        break