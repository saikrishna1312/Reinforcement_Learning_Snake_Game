# Snake Game with Deep Q-Network (DQN)
Welcome to the Snake Game with Deep Q-Network! This project applies Reinforcement Learning techniques to teach an agent (the “snake”) to play the classic Snake game. The agent learns to move around, avoid walls, and eat food, getting better with every episode. It’s a fun way to understand how AI can learn from trial and error, just like humans!

## Project Overview
This project uses a Deep Q-Network (DQN), a popular type of neural network used in reinforcement learning. Here’s a simple breakdown of the concepts:

- **Agent (Snake):** The agent is the snake in the game, which tries to collect food while avoiding collisions with walls or its own body.
- **Environment (Game):** The environment is the Snake game itself, where the snake moves on a grid, grows longer when it eats food, and "dies" if it hits a wall or itself.
- **Goal:** The agent's goal is to eat as much food as possible without dying.
- **Learning Process:** The snake learns by trying out different moves and receiving rewards:
  - **Positive Reward:** The snake gets a reward when it eats food.
  - **Negative Reward:** The snake gets penalized for hitting walls, itself, or taking too long to find food.
The Deep Q-Network (DQN) helps the snake learn the best moves by balancing exploration (trying new moves) and exploitation (using moves that have worked well in the past).

## How It Works
Here’s a simplified explanation of the workflow:

- **Observe State:** The agent (snake) observes its surroundings, such as where it is, where the food is, and if there are walls or dangers nearby.
- **Choose an Action:** Based on what it sees, the snake decides on an action (move up, down, left, or right).
- **Receive Feedback:** After the move, the snake receives feedback:
    - If it reaches food, it gets a positive reward.
    - If it collides with something, it gets a negative reward.
- **Learn from Experience:** The DQN model stores past experiences and uses them to improve its decisions over time.

## Key Components
- **DQN Model:** A neural network that helps the snake decide the best action based on its current situation.
- **Replay Memory:** Stores the snake’s past experiences, allowing it to learn from a variety of situations.
- **Epsilon-Greedy Strategy:** Balances exploring new actions with using known good moves, so the snake learns efficiently.

## Installation and Setup
To run this project, you need Python and a few additional libraries. Here’s how to get started:

**Clone the Repository:**
```
git clone https://github.com/yourusername/snake-game-dqn.git
cd snake-game-dqn
```

**Install Dependencies:** Install the necessary Python packages:
```
 pip install pygame torch numpy matplotlib
```

**Run Training:** Start training the agent (snake) by running:
```
python main.py
```
This will train the model and save it after completing the episodes.

**Test the Model:** Once training is done, you can test the snake’s performance:
```
python test.py
```

## File Structure
- **main.py:** The main script to start training the agent.
- **test.py:** The script to test the trained model and watch the snake play.
- **game/:** Contains game logic and state representation functions.
- **snake_game.py:** Manages the game environment.
- **state_representation.py:** Represents the snake’s surroundings in a way the DQN can understand.
- **model/:** Contains the DQN model and memory management.
- **dqn.py:** The neural network model.
- **replay_memory.py:** Manages the memory buffer of past experiences.
- **config/:** Holds configuration settings like learning rate, reward structure, and number of episodes.

## How to Interpret Results
As the snake trains, it goes through episodes (games). During each episode:
- The snake tries to gather food and avoid collisions.
- Rewards and penalties are tracked to measure how well the snake is learning.

When you run test.py after training, the snake should:
- Move more purposefully toward food.
- Avoid walls and its own body more effectively.

## Example Observations
- **Early Training:** The snake may seem random and hit walls often.
- **After Some Training:** It should start finding food more frequently and survive longer.
- **After Complete Training:** The snake should exhibit intelligent behavior, moving strategically toward food and avoiding hazards.

## Future Improvements
There are several ways to improve the model:
- Fine-tuning the reward structure to encourage better behavior.
- Trying more advanced versions of DQN, like Double DQN or Dueling DQN.
- Increasing the training episodes for better performance.

## Concepts Demonstrated
This project demonstrates:
- Basic reinforcement learning with a Deep Q-Network (DQN).
- Experience replay and epsilon-greedy exploration, essential for stable learning in complex environments.
- Applying neural networks to a simple game environment.

## Resources and References
This project is inspired by the research paper:

"Playing Atari with Deep Reinforcement Learning" by Volodymyr Mnih et al., which introduced the DQN algorithm.
You can read more about the DQN algorithm and its applications in reinforcement learning here (https://arxiv.org/pdf/1312.5602).
