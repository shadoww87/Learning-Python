# l = [3, -1, 4, -5, 9, 5, -3, -0, 4, -7]
# positive = []
# negative = []
# for i in range(0,len(l)):
#     if l[i] >= 0:
#         positive.append(l[i])
#     else:
#         negative.append(l[i])

# print(f"Positive : {positive}  Negative : {negative}")



# l =[10, 20, 30, 40]
# t = 0

# for i in range(0, len(l)):
#     t+= l[i]

# t = t/len(l)

# print(f"Mean : {t}")




# l = [4, 8, 45, 2, 9, 1]
# g = 0
# t = 0
# for i in range(0, len(l)):
#     if g < l[i]:
#         g = l[i]
#         t = i

# print(f"Greatest = {g} at index {t} ")



# l = [4, 8, 2, 9, 10, 65,45,34,23,78,456, 1,90]
# g = 0
# s = 0
# t = 0
# for  i in range(0, len(l)):
#     if g < l[i]:
#         g = l[i] 
#         s = l[t]
#         t = i
#     elif l[i]>s:
#         s=l[i]

# print(f"Second Greatest : {s}")



# l = [1,3,5,7,6]
# for i in range(0, len(l)-1):
#    if l[i]>l[i+1]:
#         print("Not sorted")
#         break
# else:
#     print("List is sorted")



# d1 = {"a":1}
# d2 = {"b":2}
# for i in d2:
#     d1[i]=d2[i]

# print(d1)




# d = {"a":10,"b":20,"c":30}
# t = 0 
# for i in d:
#     t+=d[i]

# print(f"Sum : {t}")



# l = ["a","b","a","c","b","a"]
# d={}
# for i in l:
#     if i in d.keys():
#         d[i]+=1
#     else:
#         d[i]=1

# print(d)


d1 = {"a":5,"b":3}
d2 = {"b":[4],"c":2}

# for i in d2:
#     if i in d1.keys():
#         d1[i]= d1[i]+d2[i]
#     else:
#         d1[i]=d2[i]

# print(d1)
d2['b'].append(3)
print(d2)