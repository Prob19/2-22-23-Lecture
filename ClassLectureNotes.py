"""
Patrick Robinson
Class lecture 2/22/23 notes


"""
myDict={"Mary":98,"Jack":78,"Patrick":85,"Harry":90,"Zach":23}
myDict["Sam"]=78
myDict["Marrie"]=92
myDict["Ria"]=88

sum=0
for i in myDict.values():
    sum+=i
    mean=sum/len(myDict)
print(mean)

myVal=myDict.values()
count=0
for i in myVal:
    if i >= 79:
        count+=1
print(count)

myList=list(myDict.values())
myList.sort()
print(myList[-1])

myDict["Sam"]=95
print(myDict)