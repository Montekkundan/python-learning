# Extracts colour form sample image
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     colors_new = (r, g, b)
#     rgb_colors.append(colors_new)
# print(rgb_colors)
import turtle as t
import random
arrow = t.Turtle()
t.colormode(255)

colour_list = [(212, 149, 95), (215, 80, 62), (47, 94, 142), (231, 218, 92), (148, 66, 91), (22, 27, 40), (155, 73, 60), (122, 167, 195), (40, 22, 29), (39, 19, 15), (209, 70, 89),
               (192, 140, 159), (39, 131, 91), (125, 179, 141), (75, 164, 96), (229, 169, 183), (15, 31, 22), (51, 55, 102), (233, 220, 12), (159, 177, 54), (99, 44, 63),
               (35, 164, 196), (234, 171, 162), (105, 44, 39), (164, 209, 187), (151, 206, 220)]
arrow.speed(0)
arrow.penup()
arrow.hideturtle()
arrow.setheading(225)
arrow.forward(300)
arrow.setheading(0)
number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):
    arrow.dot(20, random.choice(colour_list))
    arrow.forward(50)
    if dot_count % 10 == 0:
        arrow.setheading(90)
        arrow.forward(50)
        arrow.setheading(180)
        arrow.forward(500)
        arrow.setheading(0)

t.Screen().exitonclick()