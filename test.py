import torch
import time
from game.snake_game import SnakeGame
from model.dqn import DQN
from game.state_representation import get_state
from config.config import Config

def test_trained_model():
    config = Config()
    game = SnakeGame()
    
    # Initialize and load the trained DQN model
    dqn = DQN(12, config.hidden_size, 4)
    dqn.load_state_dict(torch.load('results/models/dqn_model.pth'))
    dqn.eval()  # Set to evaluation mode

    total_test_rewards = []
    num_test_episodes = 10  # Test for 10 episodes

    for episode in range(num_test_episodes):
        game.reset()
        state = torch.tensor(get_state(game), dtype=torch.float32).unsqueeze(0)
        total_reward = 0
        done = False

        while not done:
            # Select action with the trained model (exploitation only, no epsilon-greedy)
            with torch.no_grad():
                action = dqn(state).argmax().item()

            # Perform the action in the game
            game.step(action)

            # Calculate reward
            if game.snake[0] == game.food:
                reward = 50
            elif game.done:
                reward = -100
            else:
                reward = -1

            total_reward += reward

            # Render the game (optional)
            #game.render()
            #time.sleep(0.1)  # Slows down rendering for better observation

            # Move to the next state
            next_state = torch.tensor(get_state(game), dtype=torch.float32).unsqueeze(0)
            state = next_state

            if game.done:
                break

        total_test_rewards.append(total_reward)
        print(f"Test Episode {episode + 1} Reward: {total_reward}")

    # Calculate and print average test reward
    avg_test_reward = sum(total_test_rewards) / num_test_episodes
    print(f"Average Test Reward over {num_test_episodes} episodes: {avg_test_reward}")

if __name__ == "__main__":
    test_trained_model()
