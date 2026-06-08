numbers = [1,4,3,5]

length = len(numbers) + 1
set1 = set(numbers)

for num in range(1,length +1):
    if num not in numbers:
        print(num)
    