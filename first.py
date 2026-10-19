# a = (1,2,3,8,5,4,3,6,3,5,6,9,3,3,4,3,5,3)
# 
# count = a.count(3)
# print(count)

# a,h,k,j,n,m = (1,2,3,4,5,6)
# print(a)
# print(h)
# print(n)

# a = {1,2,3,4,5}
# b = {4,5,6,7,8}
# 
# print(type(a))
# union_set = a ^ b
# print(union_set)

# d1 = {1:100 , 2:200 , 3:300}
# d2 = {4:400 , 5:500 , 6:600}
# 
# for i in d2:
    # d1[i] = d2[i]
# 
# print(d1)


# a = [1,1,1,2,2,2,2,5,2,6,3,3,3,4,4,4,5,5,5,6,6,6,7,8,9]
# 
# d = {}
# for i in a:
    # if i in d.keys():
        # d[i] += 1
    # else:
        # d[i] = 1
# 
# print(d) 


# d1 = {1:100 , 2:200 , 4:300}
# d2 = {4:400 , 5:500 , 6:600}
# 
# for i in d2:
    # if i in d1.keys():
        # d1[i] += d2[i]
    # else:
        # d1[i] = d2[i]
# 
# print(d1)




# a = int(input("Enter a super number : "))
# 
# try:
    # print(10/a)
# 
# except Exception as err:
    # print(f"Sorry! There was an error as {err}")
# else:
    # print("That was a great number!!")
# 
# finally:
    # print("I do my job irrespective of your try and exception actions!!")

# name = input("What can we call you as : ")
# age = int(input("Enter your age : "))
# 
# try:
    # if (age < 10) or (age > 18):
        # raise ValueError("Your age must be between 10 to 18 only!!")
# except Exception as err:
    # print(f"There is an error in your age as {err}")
# else:
    # print(f"{name}! Welcomes You")
# finally:
    # print(f"{name} Thank You Again!!")

# p = open(r'main.py')
# print(p.read())

r = open("first.txt" , 'a')
r.write(" and I am appending somethings to the end of the file and it is what it is")
r.close()