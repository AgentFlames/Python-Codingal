list1 = [7, 42, 15, 83, 61, 29, 94, 3, 57, 76]

y=0
for i in list1:
    y = y+i

average = y/len(list1)
print(f"the average is {average}")

list1.sort()

print(list1[0])
print(list1[-1])