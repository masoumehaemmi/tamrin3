import random

ara=[]

le = (int(input("tedade ozve araye ra moshakhas konid: ")))

while le != len(ara) :


    s = random.randint(0 , 20)

    if s not in ara:
   
       
       ara.append(s)
      
print("ara:" , ara )






