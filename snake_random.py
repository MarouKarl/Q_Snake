import sys

import numpy as np
import gym
import gym_ple


class RandomAgent(object):
    # AGENT ALEATOIRE
    def __init__(self, action_space):
        self.action_space = action_space

    def act(self, observation, reward, done):
        return self.action_space.sample()





if __name__ == '__main__':

    # environnement snake
    env = gym.make('Snake-v0' if len(sys.argv) < 2 else sys.argv[1])
    env.seed(0)


    # PARAMETRES
    viz = 0 # pour activer la visualisation du jeu : 1, sinon 0
    agent = RandomAgent(env.action_space)
    episode_count = 10 # choisir le nombre de parties
    reward = 0
    done = False
    keep_reward = [] # vecteur qui contient les reward finales de chaque jeu

    for i in range(episode_count):
        ob = env.reset()

        # reward totale de la partie
        final_reward = 0

        while True:

            # pour voir le jeu sur l'interface graphique
            if viz == 1:
                env.render()

            # le serpent choisit son action
            action = agent.act(ob, reward, done)

            # variable d'etat et reward renvoyes par l'environnement
            ob, reward, done, _ = env.step(action)

            final_reward += reward

            # le jeu s'arrete quand le serpent se prend sa queue ou un mur
            if done:
                print('Reward final de la partie {} : {}'.format(i, final_reward))
                keep_reward.append(final_reward)
                break

    print('Reward moyenne de toutes les parties : {}'.format(np.mean(keep_reward)))

    env.close()