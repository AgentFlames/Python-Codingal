new_dict = {
    "codingal" : 3,
    "is" : 2 , 
    "best" : 2 , 
    "for" : 2,
    "coding" : 1
    
}

print(f"Orginal dictionary : {new_dict}")
value = 2 
count = 0 

for keys in new_dict:
    if new_dict[keys] == value:
        count += 1 

print(f"The frequency of the number 2 is : {count}")