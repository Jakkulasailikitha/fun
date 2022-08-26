#  To 
# def my_fun(num):
#     i=0
#     max=0
#     while i<len(num):
#         if max<num[i]:
#             max=num[i]
#         i=i+1
#     print(max)
# my_fun([3, 5, 7, 34, 2, 89, 2, 5])

# to find the second max in the list usinf fun
# def fun (num):
#     i=0
#     max=0
#     sec=0
#     while i<len(num):
#         if num[i]>max:
#             sec=max
#             max=num[i]
#         elif num[i]>sec:
#             sec=num[i]
#         i=i+1
#     print("the maximum num in list:",max)
#     print("the second max in list:",sec)
# fun([3, 5, 7, 34, 2, 89, 2, 5])

# to find third max  using fun
# def fun(num):
#     i=0
#     max=0
#     sec_max=0
#     third_max=0
#     while i<len(num):
#         if num[i]>max:
#             third_max=sec_max
#             sec_max=max
#             max=num[i]
#         elif num[i]>sec_max:
#             third_max=sec_max
#             sec_max=num
#             sec_max=num[i]
#         elif num[i]>third_max:
#             third_max=num[i]
#         i=i+1
#     print(max)
#     print(sec_max)
#     print(third_max)
# fun([3, 5, 7, 34, 2, 89, 2, 5])
        
# using max function directly
# fun=[3, 5, 7, 34, 2, 89, 2, 5]
# fun1=max(fun)
# print(fun1)

# def min(list):
#   current_min = list[0]  
#   for num in list:       
#     if num < current_min:
#       current_min = num 
#       print(current_min)
# min([1,2,3,-1])

def min(list):
  i=0
  num=1
  current_min = list[i]  
  while num in  list :  
    if num < current_min:
        print(current_min)
        i=i+1
min([1,2,3,-1])








#    current_min = list[0]  
#   for num in list:       
#     if num < current_min:
#       current_min = num 
#       print(current_min)
# min([1,2,3,-1])
    #   current_min = num