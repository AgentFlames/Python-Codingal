import array as a 
array_num = a.array("i" , [1,2,3,4,5,6,6,6,7])

print(array_num)

print(f"The number of times 6 occured is {array_num.count(6)}")


array_num.reverse()
print(f"the reversed array is {array_num}")