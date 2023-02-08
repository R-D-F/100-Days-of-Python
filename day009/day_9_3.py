### nesting
### nesting lists and dictionaries is like puting a folder in a folder

# nested_dictionary = {
#     key: [List],
#     key2: {dictionary},
# }

capitals = {
    "France": "Paris", 
    "Germany": "Berlin", 
}

### Nesting a List in a Dictionary

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"],
#  }

 ### You can nest a list in a list like so:

list_1 = ["A", "B", ["C", "D"]]

### but it is not as useful as a list in a dict because of the way the data is structured

### Nesting a Dictionary in a Dictionary

# travel_log = {
#     "France": {
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 12,
#         },
#     "Germany": {
#         "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#         "total_visits": 4,
#     },
# }

### nesting a ditionary inside a list
travel_log = [
    {
        "country": "France", 
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 12,
    },
    {
        "country": "Germany", 
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visits": 4,
    },
]
