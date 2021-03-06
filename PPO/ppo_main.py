import gym
from ppo_agent import PPOagent
import os
def main():
    
    max_episode_num = 100000
    env_name = 'Pendulum-v1'
    env = gym.make(env_name)
    agent = PPOagent(env)
    
    agent.train(max_episode_num)
    
    
    
    agent.plot_result()
    
if __name__ == "__main__":
    
    main()
    