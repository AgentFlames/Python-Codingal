import calendar


print("1.Print all months full names")
print("2.Print months abbrivated names")


while True:
    try:
        func = int(input("pick one of the following numbers for the fuction desired:"))
        if func == 1:
            for x in range(1,13):
                print(calendar.month_name[x])
                
            break
        
        elif func == 2:
            for x in range(1,13):
                print(calendar.month_abbr[x])
            break

        else:
            print("Enter one of the following numbers: 1 or 2")

    except ValueError:
        print("Error: Invalid Interger")
