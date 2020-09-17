# To find x's y power with recursion

def power(x, y):
    if y == 1 :
        return x
    else :
        return x * power(x, y-1)

power(2, 5)