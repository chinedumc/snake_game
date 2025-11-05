import time
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake game')
screen.tracer(0)

# starting_positions = [(0,0),(-20,0),(-40,0)]

# segments = []

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# for position in starting_positions:
#   new_segment = Turtle('square')
#   new_segment.color('white')
#   new_segment.penup()
#   new_segment.goto(position)
#   segments.append(new_segment)

# segment_1 = Turtle('square')
# segment_1.color('white')

game_is_on = True
while game_is_on:
  screen.update()
  time.sleep(0.1)

  snake.move()

  #Detect collision with food.
  if snake.head.distance(food) < 15:
    food.refresh()
    snake.extend_snake()
    scoreboard.increase_score()

  # Detect collision with wall
  if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < - 290:
    game_is_on = False
    scoreboard.game_over()

  # Detect collision with tail
  for segment in snake.segments[1:]:
    if snake.head.distance(segment) < 10:
      game_is_on = False
      scoreboard.game_over()











screen.exitonclick()