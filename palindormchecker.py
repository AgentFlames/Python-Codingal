def plaindrome(t):
    e = len(t) - 1
    s = 0

    while s<e:
        if t[s] != t[e]:
            return False
        else:
            s+=1
            e-=1

    return True

numbers = (1,2,3,4,45,3,2,1)

if plaindrome(numbers):
    print("It is a Palindrome")

else:
    print("it is not a palindrome")