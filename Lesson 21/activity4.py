phone_book = {
    "john" : "35343122342",
    "Bella" : "35346147322",
    "Poppy" : "35393925312",
}

dec = input("Who's Phone number would You like : ")
print(f"Their Phone Number is {phone_book.get(dec , "phone number not found: ")}")

delete_name = input("Enter A phone number that you would like to delete: ")

if delete_name in phone_book:
    del phone_book[delete_name]
    print("deletion successful")

else:
    print("deletion unsuccessfull. phone number not found: ")

print(phone_book)