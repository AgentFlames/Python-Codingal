list1 = ['abc','xqx',"yup","vov","12831","xz"]
validlist = []

valid = 0


for x in list1:
    if len(x) >= 3 and x[0]== x[-1]:
        valid = valid+1
        validlist.append(x)
        
print(valid)
print(validlist)



        

    
    