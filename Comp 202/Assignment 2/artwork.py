#Marie-Elise Latorre
#260981320
 
#import everything needed 
import turtle
import random
 
#eyes for my spooky face
def black_hole(x,y):
    """
    (int, int) -> void
    Draws repetive lines in circle
    """
    tom = turtle.Turtle() 
    tom.penup()
    tom.setposition(x, y)
    tom.pendown()
    tom.speed(15)
    for i in range(45):
        tom.forward(100)
        tom.right(30)
        tom.forward(20)
    
    
        tom.penup()
        tom.setposition(x, y)
        tom.pendown()
    
        tom.right(2)
        
    
def mouth(x,y):
    """
    (int, int) -> void
    Draws a helix using the users choosen colors
    """
    
    if x == 1:
        e = 'purple'
    elif x == 2:
        e = 'cyan'
    elif x == 3:
        e = 'pink'
    elif x == 4:
        e = 'lime'
        
    if y == 1:
        r = 'purple'
    elif y == 2:
        r = 'cyan'
    elif y == 3:
        r = 'pink'
    elif y == 4:
        r = 'lime'
    
    colors = [e, r]
    turtle.speed(25)
    turtle.penup()
    turtle.setposition(0,-150)
    turtle.pendown()
 
    for i in range(15):
        turtle.pencolor(colors[i%2])
        turtle.circle(5*i,360)
        turtle.circle(-5*i,360)
        turtle.left(i)
    
    
        
    turtle.hideturtle()
        
        
    return
 
def corner_of_mouth(l,o,d,e):
    '''
    (int,int,int,int) -> void
    draws an arc circle to look like the bottom of a smile
    '''
    bob = turtle.Turtle()
    bob.penup()
    bob.setposition(l,o)
    bob.pendown()
    bob.fillcolor('gray')
    bob.begin_fill()
    bob.circle(d,e)
    bob.end_fill()
    bob.hideturtle()
    
def outline(p,e,w,q):
    '''
    (int,int,int,int) -> void
    draws an arc circle to look like the top of a smile
    '''
    joe = turtle.Turtle()
    joe.penup()
    joe.setposition(p,e)
    joe.pendown()
    joe.circle(w,q)
    joe.hideturtle()
    
    
    
    
 
def nose():
    '''
    (void) -> void
    draws a triangle for the nose with a random color
    '''
    olga = turtle.Turtle()
    olga.penup()
    olga.setposition(-45, 0)
    olga.pendown()
    z = random.randint(1,4)
    if z == 1:
        r = 'purple'
    else:
        r = 'orange'
    olga.fillcolor(r) 
    olga.begin_fill() 
    
    olga.forward(100) # draw base
    olga.left(120)
    olga.forward(100)
    olga.left(120)
    olga.forward(100)
    olga.hideturtle()
    olga.end_fill()
    return
 
 
def last_name():
    '''
    (void) -> void
    Draws letter L from Latorre at the bottom right corner
    '''
    lin = turtle.Turtle()
    lin.penup()
    lin.setposition(300, -250)
    lin.pendown()
    lin.right(90)
    lin.forward(50)
    lin.left(90)
    lin.forward(30)
    lin.hideturtle()
    return
    
    
    
def my_artwork():
    '''
    (void) -> void
    Calls all the other functions to draw one big picture
    '''
    print("Colors:\n1.\tpurple")
    print("2.\tcyan")
    print("3.\tpink")
    print("4.\tlime")
    x = int(input("Choose your color (1-4):" ))
    y = int(input("Choose another color (1-4):" ))
    ted = turtle.Turtle()
    ted.speed(15)
    ted.hideturtle()
    
    mouth(x,y)
    corner_of_mouth(140,-135,99,70)
    corner_of_mouth(-140,-135,99,-70)
    outline(130,-115,140,50)
    outline(-130,-115,140,-50)
    
    
    black_hole(-200,200)
    black_hole(200,200)
    nose()
    last_name()
    return 
