country_code = { 
    "spain" : "34",
    "ireland" : "353",
    "U.K" : "44"
}

print(f"The country code of Spain is {country_code.get("spain" , "not found")}")
print(f"The country code of Japan is {country_code.get("japan" , "not found")}")