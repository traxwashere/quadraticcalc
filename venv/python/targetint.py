brolist = [4, 65, 233, 34,67,95,91,11]
avg = sum(brolist)/len(brolist)
print("The average is", round(avg,2))
brolist.sort()
print(brolist)
x = len(brolist)/2
print (x)
print(type(x))
if isinstance(x,float):
    print ("the median is",brolist[x]
