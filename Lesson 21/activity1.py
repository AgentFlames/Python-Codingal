student_data = {
    "id1" : {
        "name" : "John",
        "class" : "6th",
        "subject" : "Geography"
    },

    "id2" : {
        "name" : "Martin",
        "class" : "6th",
        "subject" : "Geography"
    },

    "id3" : {
        "name" : "John",
        "class" : "6th",
        "subject" : "Geography"
    },

    "id4" : {
        "name" : "Nicolas",
        "class" : "5th",
        "subject" : "Geography"
    },
}

results = {}
seen_keys = []

for id,details in student_data.items():
    unique_keys = (details["name"], details["class"], details["subject"] )
    if unique_keys not in seen_keys:
        seen_keys.append(unique_keys)
        results[id] = details

for k ,v in results.items():
    print(f"{k} : {v}")
