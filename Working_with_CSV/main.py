# with open("weather_data.csv") as temp_data:
#     data = temp_data.readlines()
#     # print(data)

import pandas as pd
data = pd.read_csv("squirrel_dataset.csv")
# tempreature = data["temp"]
# avg = sum(tempreature)/len(tempreature)
# print(avg)
# print(data[data.temp == tempreature.max()])
series = data["Primary Fur Color"]
color1 = 0
color2 = 0
color3 = 0
for color in series:
    if color == "NaN":
        pass

    elif color == "Gray":
        color3 += 1

    elif color == "Red":
        color2 += 1

    elif color1 == "Black":
        color1 += 1

dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [color3, color2, color1]
}

df = pd.DataFrame(dict)
df.to_csv("Squirrel_Count")
