def addition(a,b):
    c=a+b
    return(c)
def sub(a,b):
    d=a-b
    return(d)
def multiply(a,b):
    e=a*b
    return(e)
def divided(a,b):
    f=a/b
    return(f)
def main():
    if symbol=="+":
        print(addition(a,b))
    elif symbol=="-":
        print(sub(a,b))
    elif symbol=="*":
        print(multiply(a,b))
    else:
        print(divided(a,b))
a=int(input("enter the number1 here:"))
b=int(input("enter the number2 here:"))
symbol=input("enter the symbol here:")
main()      
    
# Now using input take 2 numbers input from the user.
# Call the calculator function 4 times again and again to add, substract, multifly,
# divide the two numbers and show the result in 4 different variables.
# add_result (store the add operation result)
# subtract_result (store the subtract operation result)
# multiply_result (store the multiple operation result)
# divide_result (store the divide operation result)
# Then print the above four variables.
# def addition(a,b):
#     c=a+b
#     return c
# def sub(a,b):
#     d=a-b
#     return(d)
# def multiply(a,b):
#     e=a*b
#     return(e)
# def divided(a,b):
#     f=a/b
#     return(f)  
# a=int(input("enter the number1 here:"))
# b=int(input("enter the number2 here:"))
# print(addition(a,b))
# print(sub(a,b))
# print(multiply(a,b))
# print(divided(a,b))

# part 2

# l=([5, 10, 50, 20],[2, 20, 3, 5])
# i=0
# a=[]
# while i<len(l)-1:
#     j=0
#     while j<len(l[i]):
#         c=l[i][j]*l[i+1][j]
#         j+=1
#         a.append(c)
#     i=i+1
# print(a)

# def key(l):
# # l=([5, 10, 50, 20],[2, 20, 3, 5])
#     i=0
#     a=[]
#     while i<len(l)-1:
#         j=0
#     while j<len(l[i]):
#         c=l[i][j]*l[i+1][j]
#         j+=1
#         a.append(c)
#     i=i+1
#     print(a)
# key(([5, 10, 50, 20],[2, 20, 3, 5]))