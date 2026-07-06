class pair_element: 

    def twosum(self, nums, target): 
        lookup = {}

        for i, num in enumerate(nums):
            if target - num in lookup:
                return(lookup[target-num], i)
            lookup[num] = i
numbers = (0,10,20,30,40,50,60,70,80,90,100)
value = int(input("Enter a number: "))

print("index1 = %d, index2 = %d" %pair_element().twosum(numbers,value))
