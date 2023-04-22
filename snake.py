MOVE_DISTANCE=20
STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
UP=90
DOWN=270
LEFT=180
RIGHT=0
from turtle import Turtle,Screen

class Snake():
    def __init__(self):
        self.snake_body=[]
        self.create_snake()

    def create_snake(self):
    # Create initial  snake body
        for i in STARTING_POSITIONS:
            t=Turtle()
            t.pu()
            t.goto(i)
            t.shape('square')
            t.color('yellow')
            self.snake_body.append(t)
    
    def move_snake(self):
        for i in range(len(self.snake_body)-1,0,-1):
            new_x=self.snake_body[i-1].xcor()
            new_y=self.snake_body[i-1].ycor()
            self.snake_body[i].goto(x=new_x,y=new_y)
        self.snake_body[0].fd(MOVE_DISTANCE)
    
    def up(self):
        if self.snake_body[0].heading()!=DOWN:
            self.snake_body[0].seth(UP)
    
    def down(self):
        if self.snake_body[0].heading()!=UP:
            self.snake_body[0].seth(DOWN)

    def left(self):
        if self.snake_body[0].heading()!=RIGHT:
            self.snake_body[0].seth(LEFT)

    def right(self):
        if self.snake_body[0].heading()!=LEFT:
            self.snake_body[0].seth(RIGHT)