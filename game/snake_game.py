import random

GRID_SIZE = 20
GRID_WIDTH = 20
GRID_HEIGHT = 20

class SnakeGame:
    def __init__(self):
        self.reset()

    def reset(self):
        self.snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (0, 1)
        self.spawn_food()
        self.done = False

    def spawn_food(self):
        while True:
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            if (x, y) not in self.snake:
                self.food = (x, y)
                break

    def step(self, action):
        # Map action to direction
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.direction = directions[action]

        # Move the snake
        new_head = (self.snake[0][0] + self.direction[0], self.snake[0][1] + self.direction[1])
        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.spawn_food()
        else:
            self.snake.pop()

        x, y = new_head
        if x < 0 or x >= GRID_WIDTH or y < 0 or y >= GRID_HEIGHT or new_head in self.snake[1:]:
            self.done = True

    def render(self):
        # Rendering can be added for visualization
        pass
