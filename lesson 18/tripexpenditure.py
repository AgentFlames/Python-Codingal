def hotelcost(days):
    return 200*days

def planeridecost(city):
    if "Dublin" == city:
        return 200
    elif "Paris" == city:
        return 300
    elif "Madrid" == city:
        return 250
    elif "Lisbon" == city:
        return 350
    
def rentalcarcost(days):
    if days>=7:
        return 30*days-75
    elif days>=3:
        return 30*days-40
    else:
        return 30*days
    
def tripcost(city,days,spendingamount):
    return hotelcost(days) + planeridecost(city) + rentalcarcost(days) + spendingamount

print(tripcost("Dublin",30,6000))
    

