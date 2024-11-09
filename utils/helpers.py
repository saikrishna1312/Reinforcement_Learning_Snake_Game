def decay_epsilon(epsilon, min_epsilon, decay_rate):
    return max(min_epsilon, epsilon * decay_rate)
