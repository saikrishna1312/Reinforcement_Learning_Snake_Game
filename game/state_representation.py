import numpy as np
from game.snake_game import GRID_WIDTH, GRID_HEIGHT


def get_state(game):
    head_x, head_y = game.snake[0]
    food_x, food_y = game.food

    direction_left = game.direction == (-1, 0)
    direction_right = game.direction == (1, 0)
    direction_up = game.direction == (0, -1)
    direction_down = game.direction == (0, 1)

    danger_left = (head_x - 1 < 0) or ((head_x - 1, head_y) in game.snake)
    danger_right = (head_x + 1 >= GRID_WIDTH) or ((head_x + 1, head_y) in game.snake)
    danger_up = (head_y - 1 < 0) or ((head_x, head_y - 1) in game.snake)
    danger_down = (head_y + 1 >= GRID_HEIGHT) or ((head_x, head_y + 1) in game.snake)

    food_left = food_x < head_x
    food_right = food_x > head_x
    food_up = food_y < head_y
    food_down = food_y > head_y

    state = [
        danger_left, danger_right, danger_up, danger_down,
        direction_left, direction_right, direction_up, direction_down,
        food_left, food_right, food_up, food_down
    ]

    return np.array(state, dtype=int)
