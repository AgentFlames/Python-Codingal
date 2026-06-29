school = {
    "max" : 92,
    "alice" : 52,
    "emily" : 27,
    "john" : 72,
    "zach" : 85,
          }

total = 0

for score in school.values():
    total = total + score

average = total / 5
print(f"the average score was {average}")



for student in school.keys():
    if school[student] == max(school.values()):
        print(f"{student} has the highest score in the class")

for student in school.keys():
    if school[student] == min(school.values()):
        print(f"{student} has the lowest score in the class")

search = input("Enter the name of the student you would like to search for : ")
if search not in school.keys():
    print("Error : student doesn't exist")

else:
    print(f"{search} : {school.get(search)}")