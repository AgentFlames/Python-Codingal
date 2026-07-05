a = 10 
b = 5
c = 9
print(f"a ={a}, b = {b} , c = {c}")
d = a

a = b # a = 5
b = d # b = 10

d = c # d = 9 
c = b
b = 9

print(f"a ={a}, b = {b} , c = {c}")