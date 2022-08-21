from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # to find whether the snake ate the food
    if snake.head.distance(food) < 15:
        # print("TASTy")
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # collision with wall.....
    # Wall will be an imaginary line
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 275 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # collision with snake's own segments
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
