#  in this question to find the string using user
def function(string):
    i=0
    count1=0
    count2=0
    while i<len(string):
        if string[i].isupper():
            count1=count1+1
        elif string[i].islower():
            count2=count2+1
        i=i+1
    print(count1)
    print(count2)
user=input("enter the string in here:")
function(user)
# def factorial(n):
#     if (n==0 or n==1):
#         return 1
#     else:
#         return n* factorial(n-1)
# n=int(input("enter the values:"))
# res=factorial(n)
# print(res)
