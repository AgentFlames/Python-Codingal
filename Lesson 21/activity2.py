new_dict = {
    "numbers" : 2,
    "cars" : 2 , 
    "houses" : 2,
    "phones" : 2 , 
    "headphones" : 1,
    
}

print(f"Orginal dictionary : {new_dict}")
value = 2 
count = 0 

for keys in new_dict:
    if new_dict[keys] == value:
        count += 1 

print(f"The frequency of the number 2 is : {count}")