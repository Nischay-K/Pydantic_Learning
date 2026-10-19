# def palindrome(st):
    # rev = ""
    # for i in range(len(st) - 1 , -1 , -1):
        # rev = rev + st[i]
# 
    # if (rev == st):
        # return "Palindrome!!"
    # return "Not a Palindrome!!"


# print(palindrome("NAMAN"))
# print(palindrome("ABHI"))

a = [12 , 13 , 14 , 15 , 16 , 71 , 20 , 21 , 68 , 98]

largest = a[0]
second_largest = a[0]

for i in a:
    if (i > largest):
        second_largest = largest
        largest = i
    elif (i > second_largest):
        second_largest = i

print(largest , second_largest)
