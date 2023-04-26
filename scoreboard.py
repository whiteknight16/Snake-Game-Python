from turtle import Turtle
ALIGN="center"
FONT=("Arial,24,normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("./data.txt",mode="r") as file:
            self.high_score=file.read()
        self.high_score=0
        self.color("white")
        self.hideturtle()
        self.pu()
        self.goto(0,270)
        self.update_scoreboard()
    
    
    def update_scoreboard(self):
        with open("./data.txt",mode="r") as file:
            self.high_score=file.read()
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}",align=ALIGN,font=FONT)


    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()

    
    def reset(self):
        if self.score>int(self.high_score):
            with open("./data.txt",mode="w") as file:
                  file.write('%d' %self.score)
            self.high_score=self.score
        self.score=0
        self.update_scoreboard()
