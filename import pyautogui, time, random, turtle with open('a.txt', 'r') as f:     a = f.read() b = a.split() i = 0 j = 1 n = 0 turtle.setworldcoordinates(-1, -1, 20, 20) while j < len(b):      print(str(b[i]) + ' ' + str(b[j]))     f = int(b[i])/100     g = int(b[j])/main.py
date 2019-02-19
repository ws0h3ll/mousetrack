import pyautogui, time, random, turtle
with open('a.txt', 'r') as f:
    a = f.read()
b = a.split()
i = 0
j = 1
n = 0
turtle.setworldcoordinates(-1, -1, 20, 20)
while j < len(b):

    print(str(b[i]) + ' ' + str(b[j]))
    f = int(b[i]) // 100
    g = int(b[j]) // 100
    point2 = f,g
    turtle.pendown()
    turtle.goto(point2)
    turtle.hideturtle()
    print(f)
    print(g)
    i += 2
    j += 2
    n = 1
turtle.mainloop()
def takeread():
    a = random.randint(0,1000000000)
    while 1:
        x,y=pyautogui.position()
        posstr = 'X: ' + str(x) + ' Y: ' + str(y).rjust(4)
        print(posstr)
        with open('a.txt','a') as f:
            f.write(str(x) + ' ' + str(y) + '\n')
        print('\b' * len(posstr))
        time.sleep(0.00001)
