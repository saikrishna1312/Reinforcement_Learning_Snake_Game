from game.snake_game import SnakeGame
from model.train import train_dqn
from config.config import Config

def main():
    config = Config()
    game = SnakeGame()
    train_dqn(game, config)

if __name__ == "__main__":
    main()
