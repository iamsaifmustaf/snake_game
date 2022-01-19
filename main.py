from turtle import Screen, window_height
import time
import winsound
from snake import Snake
from food import Food
from scoreboard import Scoreboard


def snake_game():

    # Create Screen and set bg color, size and title
    speed = 0.1
    screen = Screen()
    screen.clear()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    #Key Events
    screen.onkey(snake.move_up,"Up")
    screen.onkey(snake.move_down,"Down")
    screen.onkey(snake.move_left,"Left")
    screen.onkey(snake.move_right,"Right")
    screen.onkey(snake_game,"r")


    game_is_on = True
    food_count = 0
    while game_is_on:
        screen.update()
        time.sleep(speed)
        snake.move()

        #Detect collision with Food
        if snake.head.distance(food) < 15:
            winsound.PlaySound('./sounds/eat_food.wav', winsound.SND_ASYNC)
            food.new_food_location()
            snake.extend()
            scoreboard.increase_score()
            food_count += 1
        if food_count > 20:
            speed *= 0.98
        if food_count > 40:
            speed *= 0.96

        #Detect Collison with Wall
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            game_is_on = False
            scoreboard.game_over()

        #Detect collision with tail
        for square in snake.snake_body[1:]:
            if snake.head.distance(square) < 10:
                game_is_on = False

    winsound.PlaySound('./sounds/game_over.wav', winsound.SND_ASYNC)
    scoreboard.game_over()

    screen.mainloop()


snake_game()
