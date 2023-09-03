import turtle
import time
import random

posponer = 0.1

#ventana
ventana=turtle.Screen()
ventana.title("Snake Game")
ventana.bgcolor("green")
ventana.setup(width=600, height=600)
ventana.tracer(0)

#serpiente
snake=turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.penup()
snake.goto(0,0)
snake.color("blue")
snake.direccion="abajo"

#comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.penup()
comida.goto(0,100)
comida.color("red")


#texto-
texto = turtle.Turtle()
texto.speed(0)
texto.color("purple")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Score: 0      High_score: 0", align = "center", font = ("courier", 24, "normal"))
#marcador---
score = 0
high_score = 0

def movimiento():
    if snake.direccion == "arriba":
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direccion == "abajo":
        y = snake.ycor()
        snake.sety(y - 20)

    if snake.direccion == "derecha":
        x = snake.xcor()
        snake.setx(x + 20)

    if snake.direccion == "izquierda":
        x = snake.xcor()
        snake.setx(x - 20)

#funciones para el teclado
def arriba():
    snake.direccion = "arriba"
def abajo():
    snake.direccion = "abajo"
def derecha():
    snake.direccion = "derecha"
def izquierda():
    snake.direccion = "izquierda"

ventana.listen()
ventana.onkeypress(arriba, "Up")
ventana.onkeypress(abajo, "Down")
ventana.onkeypress(derecha, "Right")
ventana.onkeypress(izquierda, "Left")

segmentos = []


while True:
    ventana.update()
    #colicion bordes

    if snake.xcor() > 280 or snake.xcor() < -280 or snake.ycor() > 280 or snake.ycor() < -280:
        time.sleep(1)
        snake.goto (0,0)
        snake.direction = "stop"

        # Borrar los segmentos.
        for segmento in segmentos:
            segmento.hideturtle()
            segmento.goto(1000,1000)

        #Limpiar lista de segmentos
        segmentos.clear()
         #resetear marcador
        score = 0
        texto.clear()
        texto.write("Score: {}      High_score: {}".format(score, high_score), align = "center", font = ("courier", 24, "normal"))


    #--- colisión comida
    if snake.distance(comida) < 20:
        #posisción random
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        comida.goto(x,y)


        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape('square')
        nuevo_segmento.penup()
        nuevo_segmento.goto(0,0)
        nuevo_segmento.direction = 'stop'
        nuevo_segmento.color('cyan')
        segmentos.append(nuevo_segmento)

        score += 10

        if score > high_score:
            high_score = score
           
            #colores
            if score >= 0:
                texto.color("purple")
            if score >= 50:
                texto.color("red")
            if score >= 100:
                texto.color("brown")
            if score >= 200:
                texto.color("gray")
            if score >= 300:
                texto.color("yellow")

        texto.clear()
        texto.write("Score: {}      High_score: {}".format(score, high_score), align = "center", font = ("courier", 24, "normal"))

#movimiento del cuerpo---333333
    totalSeg = len(segmentos)

    for index in range(totalSeg -1, 0, -1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x,y)

    if totalSeg > 0:
        x = snake.xcor()
        y = snake.ycor()
        segmentos[0].goto(x,y)
    movimiento()



    #colision cuerpo

    for segmento in segmentos:
        if segmento.distance(snake) < 20:
            time.sleep(1)
            snake.goto(0,0)
            snake.direction = "stop"

            #borrar segmentos
            for segmento in segmentos:
                segmento.hideturtle()
            segmentos.remove(nuevo_segmento)
            #limpiar segmentos
            segmentos.clear()
            
            score = 0
            texto.clear()
            texto.write("Score: {}      High_score: {}".format(score, high_score), align = "center", font = ("courier", 24, "normal"))


    time.sleep(posponer)
