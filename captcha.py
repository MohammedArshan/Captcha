import tkinter as tk
import random as r

root = tk.Tk()

root.title("CAPTCHA")

canvas1 = tk.Canvas(root, width = 400, height = 400,  relief = 'raised')
canvas1.pack()

heading = tk.Label(root, text = 'CAPTCHA')
heading.config(font = ('helvetica', 14))
canvas1.create_window(200, 10, window = heading)

instructions = tk.Label(root, text = 'Enter the shape and color in which the expression is correct')
instructions.config(font = ('helvetica', 10))
canvas1.create_window(200, 40, window = instructions)

def createRandomUniqueList(num, start, end):
	arr = []
	tmp = r.randint(start, end)
	for x in range(num):
		while tmp in arr:
			tmp = r.randint(start, end) 
		arr.append(tmp) 	
	return arr

coordinates = [[60, 60, 150, 150], [160, 60, 280, 150], [290, 60, 380, 150]]
color = ['red', 'green', 'blue', 'yellow', 'orange']
color_list = createRandomUniqueList(5, 0, 4)
index_list = createRandomUniqueList(3, 0, 2)

canvas1.create_rectangle(coordinates[index_list[0]][0], coordinates[index_list[0]][1], coordinates[index_list[0]][2], coordinates[index_list[0]][3], fill = color[color_list[index_list[0]]])
canvas1.create_rectangle(coordinates[index_list[1]][0], coordinates[index_list[1]][1], coordinates[index_list[1]][2], coordinates[index_list[1]][3], fill = color[color_list[index_list[1]]])
canvas1.create_oval(coordinates[index_list[2]][0], coordinates[index_list[2]][1], coordinates[index_list[2]][2], coordinates[index_list[2]][3], fill = color[color_list[index_list[2]]])

operators = ["+","-","*"]
num1, num2, operation = r.randint(1, 10), r.randint(1, 10), r.choice(operators) 
val = eval(str(num1) + operation + str(num2))
exp = [str(num1) + ' ' + operation + ' '  + str(num2) + ' = ' + str(val), str(num1) + ' ' + operation + ' '  + str(num2) + ' = ' + str(val + r.randint(1, 10)), str(num1) + ' ' + operation + ' '  + str(num2) + ' = ' + str(val - r.randint(1, 10))]

# print(index_list)
# print(index_list.index(0))
# print(coordinates[index_list.index(0)][0])
# print(color)
# print(color_list)
# print(color[index_list.index(0)])
# print(color[index_list[0]], color[index_list[1]], color[index_list[2]])

exp1 = tk.Label(root, text = exp[index_list[0]])
exp1.config(font = ('helvetica', 10))
canvas1.create_window(105, 105, window = exp1)
exp2 = tk.Label(root, text = exp[index_list[1]])
exp2.config(font = ('helvetica', 10))
canvas1.create_window(220, 105, window = exp2)
exp3 = tk.Label(root, text = exp[index_list[2]])
exp3.config(font = ('helvetica', 10))
canvas1.create_window(335, 105, window = exp3)

shape_text = tk.Label(root, text = 'Enter Shape:')
shape_text.config(font = ('helvetica', 10))
canvas1.create_window(100, 200, window = shape_text)

shape_text_box = tk.Entry (root) 
canvas1.create_window(100, 240, window = shape_text_box)

color_text = tk.Label(root, text = 'Enter Color:')
color_text.config(font = ('helvetica', 10))
canvas1.create_window(300, 200, window = color_text)

color_text_box = tk.Entry (root) 
canvas1.create_window(300, 240, window = color_text_box)

def checkShapeColor():
    
    shape_input = shape_text_box.get()
    color_input = color_text_box.get()

    right_ans = index_list.index(0)
    # print(right_ans)
    x1, y1, x2, y2 = coordinates[right_ans][0], coordinates[right_ans][1], coordinates[right_ans][2], coordinates[right_ans][3]
    c = color[color_list[right_ans]]
    # print(x1, y1, x2, y2, c)
    if x1 - x2 == y1 - y2:
        s = 'square'
    else:
        s = 'rectangle'
    
    if shape_input == s and color_input == c :
    
        human = tk.Label(root, text = 'Human',font = ('helvetica', 10))
        canvas1.create_window(200, 310, window = human)
    
    else:

        robot = tk.Label(root, text = "Robot",font = ('helvetica', 10))
        canvas1.create_window(200, 310, window = robot)
    
shape_color_input = tk.Button(text = 'Input Shape and Color', command = checkShapeColor, bg = 'black', fg = 'white', font = ('helvetica', 9, 'bold'))
canvas1.create_window(200, 280, window = shape_color_input)

root.mainloop()