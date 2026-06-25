from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("China Provinces Map Quiz")
image = "China_blank_map.gif" #image has to be .gif
screen.addshape(image)
background = Turtle()
background.shape(image)

label = Turtle()
label.hideturtle()
label.penup()

#List of provinces:
provinces_text = "Anhui, Beijing, Chongqing, Fujian, Gansu, Guangdong, Guangxi, Guizhou, Hainan, Hebei, Heilongjiang, Henan, Hong Kong, Hubei, Hunan, Inner Mongolia, Jiangsu, Jiangxi, Jilin, Liaoning, Macau, Ningxia, Qinghai, Shaanxi, Shandong, Shanghai, Shanxi, Sichuan, Taiwan, Tianjin, Tibet, Xinjiang, Yunnan, Zhejiang"
provinces_list = provinces_text.split(", ") #Split the text by comma + space into a list
china_provinces = pd.read_csv("Coordinates.csv")
guessed_list = []

#Method for check if guess is in the province list.
def check_guess(guess):
    if guess in provinces_list and guess not in guessed_list:
        guessed_list.append(guess)
        row = china_provinces[china_provinces.Province == guess]
        x_cor = row["x"].item()
        y_cor = row["y"].item()
        label.goto(x_cor, y_cor)
        label.write(f"{guess}", align='left', font=('Courier', 8, 'bold'))
        return True
    else:
        return False

#Keep score, set rule for exit, none, answering all provinces.
game_is_on = True

while game_is_on:
    score = len(guessed_list)
    answer = screen.textinput(title=f"{score} out of 34", prompt="Enter a province:")
    if answer is None: #user clicks cancel game
        break #exit loop immediately, game_is_on = False still runs the loop
    elif answer.title().strip() == "Exit":
        provinces_to_learn = []
        for item in provinces_list:
            if item not in guessed_list:
                provinces_to_learn.append(item)
        df = pd.DataFrame(provinces_to_learn, columns=["Province"])
        df.to_csv("provinces_to_learn.csv", index=False)
        break
    else:
        check_guess(answer.title().strip())

    if len(guessed_list) == 34:
        game_is_on = False


# Get (x,y) for each province:
# coordinates = []
# current_index = 0
# screen.title(f"Click: {provinces_list[current_index]}")
#
# def get_province_cor(x,y):
#     global current_index
#     if current_index < len(provinces_list):
#         province = provinces_list[current_index]
#         coordinates.append({
#             "Province": province,
#             "x": x,
#             "y": y
#         })
#         current_index += 1
#         screen.title(f"Click: {provinces_list[current_index]}")
#
#
#     else:
#         screen.title("Finished")
#
# screen.onscreenclick(get_province_cor)
# screen.mainloop()
# df = pandas.DataFrame(coordinates) #turn list to dataframe
# df.to_csv("Coordinates.csv")
