import torch
import torch.optim as optim
import torch.nn.functional as F
import random
from model.dqn import DQN
from model.replay_memory import ReplayMemory
from game.state_representation import get_state
import matplotlib.pyplot as plt

def train_batch(dqn, memory, optimizer, config):
    if len(memory) < config.batch_size:
        return  # Ensure there are enough experiences to sample a full batch

    batch = memory.sample(config.batch_size)
    states, actions, rewards, next_states, dones = zip(*batch)

    states = torch.cat(states)
    actions = torch.tensor(actions).unsqueeze(1)
    rewards = torch.tensor(rewards, dtype=torch.float32)
    next_states = torch.cat(next_states)
    dones = torch.tensor(dones, dtype=torch.float32)

    # Calculate Q-values for the current states
    q_values = dqn(states).gather(1, actions)

    # Calculate target Q-values for the next states
    max_next_q_values = dqn(next_states).max(1)[0].detach()
    target_q_values = rewards + (config.gamma * max_next_q_values * (1 - dones))

    loss = F.mse_loss(q_values, target_q_values.unsqueeze(1))

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

def train_dqn(game, config):
    dqn = DQN(12, config.hidden_size, 4)
    optimizer = optim.Adam(dqn.parameters(), lr=config.lr)
    memory = ReplayMemory(config.memory_capacity)

    for episode in range(config.num_episodes):
        game.reset()
        state = torch.tensor(get_state(game), dtype=torch.float32).unsqueeze(0)
        total_reward = 0
        for step in range(config.max_steps):
            action = dqn(state).argmax().item() if random.random() > config.epsilon else random.choice([0, 1, 2, 3])
            game.step(action)
            if game.snake[0] == game.food:  
                reward = 50  
            elif game.done: 
                reward = -100  
            else: 
                reward = -1  
            total_reward += reward
            next_state = torch.tensor(get_state(game), dtype=torch.float32).unsqueeze(0)
            memory.push((state, action, reward, next_state, game.done))
            state = next_state

            if len(memory) >= config.batch_size:
                train_batch(dqn, memory, optimizer, config)

            if game.done:
                break
        print(f"Episode {episode} Reward: {total_reward}")

    torch.save(dqn.state_dict(), 'results/models/dqn_model.pth')
    print("Model saved successfully.")
