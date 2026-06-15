numbers1 = [3,5,7]
numbers2 = [6,4,2]

result = list(map(lambda x,y : x + y , numbers1 , numbers2))
print(result)


num = [1,2,3,4,5,6]

def sq(n):
    return n*n

print(list(map(sq,num)))

