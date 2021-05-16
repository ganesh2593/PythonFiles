playerList=["dhoni",3,89,"kohli","ashwin",5,3,2,7,"wefew","ewfef",8,8]

# use cases:

def stringReverse(strVal):
    str=""
    for s in strVal:
        str=s+str
    return str;

listVal=[]

for x in playerList:
    if type(x) is str:
        # print('List==>',''.join(reversed(x)))
        listVal.append(stringReverse(x))
    if type(x) is int:
         listVal.append(x)

print(listVal)



