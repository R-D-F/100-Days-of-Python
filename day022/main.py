from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("PONG")

paddle_positon_right = ((screen.window_width()/2)-20)
paddle_positon_left = -((screen.window_width()/2)-20)
paddle_right = Paddle(x_pos= paddle_positon_right)
paddle_left = Paddle(x_pos= paddle_positon_left)
score = Score()
ball = Ball()
ball.set_heading()
game_is_on = True
score_l = 0
score_r = 0 
score.right(score_r)
score.left(score_l)


while game_is_on:
    
        
    ball.move()
    ball.detect_wall_colision()
    
    ball.detect_colision_with_paddle(paddle_right, paddle_left)
    screen.listen()
    screen.onkey(paddle_right.move_up, "Up")
    screen.onkey(paddle_right.move_down, "Down")
    screen.onkey(paddle_left.move_up, "w")
    screen.onkey(paddle_left.move_down, "s")
    if ball.xcor() > 400:
        score_l += 1 
        score.clear()
        score.right(score_r)
        score.left(score_l)
        
        ball.reset()
        ball.set_heading()
    if ball.xcor() < -400:
        score_r += 1 
        score.clear()
        score.right(score_r)
        score.left(score_l)
        
        ball.reset()
        ball.set_heading()
    if score_l == 3 or score_r == 3:
        score.goto(0,0)
        score.write("Game Over")
        game_is_on = False




screen.exitonclick()