import os, sys

import gym
import gym_ple

# The world's simplest agent!
class RandomAgent(object):
    def __init__(self, action_space):
        self.action_space = action_space

    def act(self, observation, reward, done):
        return self.action_space.sample()

if __name__ == '__main__':

    env = gym.make('Snake-v0' if len(sys.argv)<2 else sys.argv[1])

    env.seed(0)
    agent = RandomAgent(env.action_space)

    episode_count = 1
    reward = 0
    done = False

    for i in range(episode_count):
        ob = env.reset()

        while True:
            env.render()
            print(ob)
            action = agent.act(ob, reward, done)
            ob, reward, done, _ = env.step(action)
            if done:
                break

    env.close()