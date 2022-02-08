# implemented by github.com/amirhosseinh77

import numpy as np
import matplotlib.pyplot as plt
from elements.model import MultiAgent, FirstOrderMultiAgent
from elements.assets import *

Nt = 1000
RANGE = 12
DISTANCE = 10
NUMBER_OF_AGENTS = 30
multi_agent_system = MultiAgent(number=NUMBER_OF_AGENTS)
# print(multi_agent_system.agents)

C1_alpha = 3
C2_alpha = 2 * np.sqrt(C1_alpha)
C1_gamma = 5
C2_gamma = 0.2 * np.sqrt(C1_gamma)

# plotting agents
# for t in range(Nt):
while True:
    adjacency_matrix = get_adjacency_matrix(multi_agent_system.agents, RANGE)
    u = np.zeros((NUMBER_OF_AGENTS,2))
    for i in range(NUMBER_OF_AGENTS):
        agent_p = multi_agent_system.agents[i,:2]
        agent_q = multi_agent_system.agents[i,2:]
        # term1
        neighbor_idxs = adjacency_matrix[i]
        if sum(neighbor_idxs)>1:
            neighbors_p = multi_agent_system.agents[neighbor_idxs,:2]
            neighbors_q = multi_agent_system.agents[neighbor_idxs,2:]
            n_ij = get_n_ij(agent_p, neighbors_p)

            term1 = C2_alpha * np.sum(phi_alpha(sigma_norm(neighbors_p-agent_p))*n_ij, axis=0)
            # term2
            a_ij = get_a_ij(agent_p, neighbors_p)
            term2 = C2_alpha * np.sum(a_ij*(neighbors_q-agent_q), axis=0)

            # u_alpha
            u_alpha = term1 + term2
        else:
            u_alpha=0
        u_gamma = -C1_gamma*sigma_1(agent_p-[50,50]) -C2_gamma*(agent_q-0)
        u[i] = u_alpha+u_gamma



    multi_agent_system.update_state(u)
    plt.cla()
    plt.axis([0, 100, 0, 100])

    for i in range(NUMBER_OF_AGENTS):
        for j in range(NUMBER_OF_AGENTS):
            if i!= j and adjacency_matrix[i,j] == 1:
                plt.plot(multi_agent_system.agents[[i,j],0], multi_agent_system.agents[[i,j],1])

    for i, (x, y,_,_) in enumerate(multi_agent_system.agents):
        plt.scatter(x, y, c='black')

    plt.pause(0.01)

plt.show()
