# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

s = input("Enter your string : ")
k = int(input("Please enter your distinct number : "))

def longest(s, k) :
    lst = []
    
    for i in range(len(s)-1) :
        string = ""
        cnt = 0
        for j in s[i:]:
            
            if j not in string :
                cnt += 1
                if cnt > k :
                    break
            string += j
           
                    
        lst.append(string.strip())
        print(lst)
    return max(lst, key=lambda x: len(x))

longest(s, k)
