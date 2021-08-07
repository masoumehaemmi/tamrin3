
araye=[]


cou= int (input("enter your count array :"))


for i in range (cou):

    ozv = int(input("enter your member :"))

    araye.append(ozv)
flag= True
for  i in range (len(araye) -1 ) :
    if araye[i] > araye [i+1] :
        flag=False
        break
if flag:
    print ('sort')    
else :
    print("no sort")
print(araye)    
