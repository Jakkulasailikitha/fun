# Use the min function and find the minimun value of the list.
# list = [8, 6, 4, 8, 4, 50, 2, 7]
# list1=min(list)
# print(list1)

# with out using min method
# lst = [10, 1,2,3,4,5]
# ans = lst[0]
# i=0
# while i<len(lst):
#     if lst[i] < ans:
#         ans = lst[i]
#     i+=1
# print(ans)

#  in function
def lock(list):
    ans = list[0]
    i=0
    while i<len(list):
        if list[i] < ans:
            ans = list[i]
        i+=1
    print(ans)
lock([10,1,2,3,4,5])




