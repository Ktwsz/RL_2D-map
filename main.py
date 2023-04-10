from environment import Environment
from model import Model

import torch.optim as optim
import torch as torch

def main():
    env_size = 10
    m = Model(env_size*env_size, 4, 0.9, 0.6, -0.000001)
    env = Environment(env_size)

    optimizer = optim.Adam(m.parameters(), lr=0.01)

    for epoch in range(100000):
        for t in range(env_size*2):
            
            done = m.policy(env)
            
            if done == 1:
                break
        loss = m.train(optimizer)
        print(epoch, loss)
        env.reset()
        env.set_random_position()
    
    torch.save(m.net.state_dict(), "model.pt")
    

if __name__ == '__main__':
    main()