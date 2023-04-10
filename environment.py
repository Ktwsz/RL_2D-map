import pygame
from time import sleep
import numpy as np

class Environment():
    def __init__(self, size):
        self.size = size
        self.showcase = False
        self.reset()

        pygame.init()
        self.screen = pygame.display.set_mode((600,600))
        self.screen.fill((255, 255, 255))
        self.rect_size = 30

    def reset(self):
        self.position = (0, 0)
        self.vector = [[0 for i in range(self.size)] for j in range(self.size)]
        self.vector[0][0] = 1

    def action(self, action):
        old_pos = self.position

        self.update_position(action)
        reward = 0
        done = 0

        if old_pos[0] == self.position[0] and old_pos[1] == self.position[1]:
            reward = -1
        elif action == 2 or action == 3:
            reward = 1
        else:
            reward = -2
        if self.position[0] == self.size-1 and self.position[1] == self.size-1:
            done = 1

        if self.showcase: self.show_state()
        return reward, np.array(self.vector).flatten(), done
    
    def get_state(self):
        return np.array(self.vector).flatten()
    
    def update_position(self, action):
        self.vector[self.position[0]][self.position[1]] = 0

        if action % 2 == 0:
            new_pos = self.position[0]+action-1
            if new_pos < 0: new_pos = 0
            elif new_pos > self.size-1: new_pos = self.size-1
            self.position = (new_pos, self.position[1])
        else:
            new_pos = self.position[1]+action-2
            if new_pos < 0: new_pos = 0
            elif new_pos > self.size-1: new_pos = self.size-1
            self.position = (self.position[0], new_pos)
        self.vector[self.position[0]][self.position[1]] = 1

    def set_random_position(self):
        self.position = (int(np.random.rand()*self.size), int(np.random.rand()*self.size))

    def draw_rect(self, color, x, y):
        pygame.draw.rect(self.screen, color, pygame.rect.Rect(x+5, y+5, self.rect_size, self.rect_size))
        pygame.draw.rect(self.screen, (0, 0, 0), pygame.rect.Rect(x+4, y+4, self.rect_size+2, self.rect_size+2), width=1)

    def show_state(self):
        for i in range(10):
            for j in range(10):
                if self.vector[i][j] == 0:
                    color = (0, 255, 0)
                else:
                    color = (255, 0, 0)
                self.draw_rect(color, 5+i*(self.rect_size+10), 5+j*(self.rect_size+10))
        pygame.display.update()
        sleep(0.2)

def main():
    
    env = Environment(10)
    env.showcase = True
    for j in range(3):
        for i in range(4):
            env.action(i)
            sleep(0.5)

if __name__ == '__main__':
    main()

