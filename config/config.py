class Config:
    def __init__(self):
        self.lr = 0.0005
        self.hidden_size = 64
        self.memory_capacity = 50000
        self.batch_size = 128
        self.num_episodes = 1000
        self.max_steps = 200
        self.epsilon = 1.0
        self.min_epsilon = 0.01
        self.epsilon_decay = 0.999
        self.gamma = 0.95
