from turtle import Turtle, Screen

FONT = ("Courier", 24, "normal")


class Scoreboard:
    def __init__(self) -> None:
        self.score = 0
        self.scorecard = Turtle()
        self.scorecard.penup()
        self.scorecard.hideturtle()
        self.scorecard.goto(-295, 260)
        self.update_score()
        

    def update_score(self):
        self.scorecard.clear()
        self.scorecard.write(f"Score: {self.score} ", font=FONT)
    
    def game_over(self):
        self.scorecard.goto(-100,0)
        self.scorecard.write("Game-Over!", font=FONT)        
    









