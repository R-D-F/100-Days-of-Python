import pandas

data = pandas.read_csv("squirrel/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

color_list = data["Primary Fur Color"].to_list()
num_black = color_list.count("Black")
num_cinnamon = color_list.count("Cinnamon")
num_gray = color_list.count("Gray")


data_dict = {
    "Fur Color": ["Black", "Red", "Gray",],
    "Count": [num_black, num_cinnamon, num_gray],
}

squirrel_color_count = pandas.DataFrame(data_dict)
squirrel_color_count.to_csv("squirrel_count.csv")