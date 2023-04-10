from environment import Environment
from model import Model
import torch


env_size = 10

m = Model(env_size*env_size, 4, 0.9, 0.0, -0.000001)
m.net.load_state_dict(torch.load("model_start_random.pt"))

env = Environment(env_size)
env.showcase = True

for i  in range(10):
    for j in range(10):
        env.position = (i, j)
        for t in range(10*env_size):
            done = m.policy(env)
            if done == 1:
                break
        env.reset()
