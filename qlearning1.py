import gym
import numpy as np

env = gym.make("MountainCar-v0")
env.reset()
done = False

DISCRETE_OS_SIZE = [20] * len(env.observation_space.high)
discrete_os_win_size = (env.observation_space.high -
                        env.observation_space.low)/DISCRETE_OS_SIZE

print(discrete_os_win_size)



# print(env.observation_space.high)
# print(env.observation_space.low)
# print(env.action_space.n)

while not done:
    action = 2

    newState, reward, done, _ = env.step(action)
    # print(newState)
    env.render()

env.close()
