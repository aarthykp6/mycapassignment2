# print positive Numbers in a List
li=[]
n=int(input("Enter size of list "))
for i in range(0,n):
    e=int(input("Enter element of list "))
    li.append(e)
print("Positive numbers in list",li,"are: ")
pos_num = list(filter(lambda x: (x>=0),li))  
print(pos_num)
#output
#Enter the size of list:4
#Enter element of list:12
#Enter element of list:14
#Enter element of list:-95
#Enter element of list:3
#positive numbers in list [12, 14, -95, 3] are:
#Output [12, 14, 3]