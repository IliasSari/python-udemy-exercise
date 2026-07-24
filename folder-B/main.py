capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

#Nested lists in dictionary

#travel_log = {
#    "France": ["Paris", "Lille", "Dijon"],
#    "Germany": ["Stuttgart", "Berlin"],
#}

#print (travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

travel_log = {
    "France":{
        "cities visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },   
    "Germany":{
        "cities visited": ["Stuttgart", "Berlin"],
        "total visits": 5
    }, 
}

print(travel_log["Germany"]["cities visited"][1])
print(travel_log["France"]["cities visited"][2])