import numpy as np
import matplotlib.pyplot as plt

# p_dot = q
# q_dot = u

# Semi-Implicit Euler Method

class MultiAgent:
    def __init__(self, number, sample_time=0.1):
        self.dt = sample_time
        self.agents = np.random.randint(0,100,(number,2)).astype('float')
        self.agents = np.hstack([self.agents, np.zeros((number,2))])

    def update_state(self, u):
        q_dot = u
        self.agents[:,2:] += q_dot * self.dt
        p_dot = self.agents[:,2:]
        self.agents[:,:2] += p_dot * self.dt
        # p_dot = self.agents[:,2:]
        # 
        # self.agents += self.dt*np.hstack([p_dot, q_dot])
        # p_dot = self.agents[:,2:]
        # q_dot = u
        # self.agents += self.dt*np.hstack([p_dot, q_dot])

class FirstOrderMultiAgent:
    def __init__(self, number, sample_time=0.1):
        self.dt = sample_time
        self.agents = np.random.randint(0,100,(number,2)).astype('float')

    def update_state(self, u):
        p_dot = u
        self.agents += self.dt*p_dot


