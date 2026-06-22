# num = int(input("Enter a number: "))
# odd = list(filter(lambda x: x % 2 != 0 , range(1,num+1) ))
# print(odd)

fruits = ["banana" , "orange" , "watermelon" , "mango" , "strawberry"]
for i in range(len(fruits)):
    fruits[i] = fruits[i].title()

print(fruits)