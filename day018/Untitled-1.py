

import colorgram



colors = colorgram.extract('damien-hirst-bromobenzotrifluoride.jpg', 10)
list_color = list(colors)
print(list_color)
first_color = list_color[0]
print(first_color.rgb)
rgb = list_color[0].rgb
r = rgb.r
g = rgb.g
b = rgb.b
print(r)