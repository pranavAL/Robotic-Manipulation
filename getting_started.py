'''
Basics of real_robots simulator. How to use a random policy to
do random tasks.
'''
import gym
import numpy as np
import time
import real_robots
from real_robots.policy import BasePolicy

class RandomPolicy(BasePolicy):
    def __init__(self, action_space):
        self.action_space = action_space
        self.action = action_space.sample()

    def step(self, action, reward, done):
        if np.random.rand() < 0.05:
            self.action = self.action_space.sample()
        return self.action

env = gym.make("REALRobot2020-R2J3-v0")
pi = RandomPolicy(env.action_space)
env.render("human")

observation = env.reset()
reward, done = 0, False
for t in range(4000):
    action = pi.step(observation, reward, done)
    observation, reward, done, info = env.step(action)
