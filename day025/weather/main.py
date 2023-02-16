import pandas

# data = pandas.read_csv("weather\weather_data.csv")
# data_dict = data.to_dict()
#print(data_dict)

# temp_list = data["temp"].to_list()


# temp_list_max = data.temp.max()
# print(temp_list_max)


# Get Data in row
#print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]

# temp_c =int(monday.temp)
# print(temp_c)
# temp_f = (temp_c * 9/5) + 32
# print(temp_f)

# create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)

print(data)