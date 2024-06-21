#print non repeating character with built in function
l=[2,1,7,2,4,7,5]
empty_list=[]
for i in l:
    if l.count(i)==1:
        empty_list.append(i)
print(empty_list)
#print non repeating character without built in function
l=[2,1,7,2,4,7,5]
empty_list=[]
for i in range(len(l)):
    if (l[i] not in l[i+1:]) and (l[i] not in l[:i]):
        empty_list.append(l[i])
print(empty_list)