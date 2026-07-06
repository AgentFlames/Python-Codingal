i = 0
k = 5
while i <= k :
    print(" " * k, end="")
    for j in range(i):
        print("*", end ="")

    print()

    i +=1
    k -= 1