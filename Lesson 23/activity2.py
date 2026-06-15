s1 = {1,2,3,4}
s2 = {"a", "b","c" ,"d"}
s3 = {"!" , "@", "£" ,"$"}
s4 = list(zip(s1,s2,s3))
print(s4)

list1 = [10,20,30,40,50]
list2 = [500,400,300,200,100]

for x,y in zip(list1,list2[::-1]):
    print(x,y)

stocks = ["SpaceX","Apple","Google"]
prices = [150 , 333 , 400]
new_dict = {stocks : prices for stocks,prices in zip(stocks,prices) }
print(new_dict)