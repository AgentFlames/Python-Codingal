different = (1, 0.99, "hi", "c", True )
print(different)

integer = (0,1,2,3,4,5,6,7,8,9,0)
print(integer)

newTuple = (9,)
print(newTuple)

combined = integer + newTuple
print(combined)


occur = 0
for new in integer:
    if new == 0:
        occur = occur +1

print(f"0 occured {occur} times")

print(integer[2:9])
