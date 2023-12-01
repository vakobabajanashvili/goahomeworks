from turtle import*

width(5)
speed(50)

def otxkutxedi():
    for i in range(4):
        forward(100)
        left(90)
otxkutxedi()

penup()
goto(100, 100)
pendown()
otxkutxedi()

penup()
goto(-100, -100)
pendown()
otxkutxedi()

penup()
left(90)
forward(200)
pendown()
def kubiki():
    for i in range(4):
        forward(100)
        right(90)
kubiki()

penup()
right(90)
forward(200)
right(90)
forward(100)
pendown()
def kubikuri():
    for i in range(4):
        forward(100)
        left(90)
kubikuri()
exitonclick()

kvadratis_gverdi = int(input("შეიყვანეთ კვადრატის გვერდი პერიმეტრის გამოსათვლელად: "))
kvadratis_gverdi1 = int(input("შეიყვანეთ კვადრატის გვერდი ფართობის გამოსათვლელად: "))
print("კვადრატის პერიმეტრია ", kvadratis_gverdi + kvadratis_gverdi)
print("კვადრატის ფართობია ", kvadratis_gverdi1 * kvadratis_gverdi1)