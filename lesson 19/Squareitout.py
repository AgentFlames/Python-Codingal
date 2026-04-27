squares = []
odd = []
even = []

starting = int(input("Enter the starting value: "))
ending = int(input("Enter the ending value: "))

for x in range(starting,ending+1):
    squares.append(x**2)

for y in squares:
    if y%2 == 0:
        even.append(y)

    else:
        odd.append(y)

print(squares)
print(odd)
print(even)