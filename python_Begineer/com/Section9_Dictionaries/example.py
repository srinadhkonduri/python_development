# tasking a dictionary

dictionary = {
    "srinadh": "handsome",
    "srinadh2": "singer"
}
# retriving items from dictionary
# print(dictionary["srinadh"])
# print(dictionary["srinadh2"])

# adding new items from the dictionary

dictionary["loop"] = "a method that runs many times"

print(dictionary)

# looping through a dictionary

for key in dictionary:
    print(key)
    print(dictionary[key])

    # nested dictionary in dictionaries

nested_dictionary = {
    "france": {
        {"cities_visited": ["paris", "lille", "dejhog"]}
    }
}

print(nested_dictionary["france"])

# nesting dictionary in a list

travel_log = [
    {
        "france": "paris",
        "cities" :["humburg","lille","effiel tower"],
        "language": "french"
    },
    {
        "india" : "delhi",
        "cities": ["nagpur","mizoram","nepal"],
        "language" : "hindi"
    }
]
