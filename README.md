# Flocking for Multi-Agent Systems
This repository contains python implementation of "Flocking for multi-agent dynamic systems: Algorithms and theory" by Olfati-Saber, Reza.
You can find the article using these links: [IEEE](https://ieeexplore.ieee.org/abstract/document/1605401), [PDF](https://sci-hub.yncjkj.com/10.1109/TAC.2005.864190)

## Algorithm
The purpose of the algorithm is to provide a common control law to form agents in a triangular shape.
**The agent model** is a double integrator:
```math
\left\{\begin{matrix}
\dot{p} = q \\
\dot{q} = u
\end{matrix}\right.
```
```p: position, q: velocity```

## Results
![Decentralized flocking](https://user-images.githubusercontent.com/56114938/148604364-b6553929-3468-4491-b473-babe69609b35.gif)
