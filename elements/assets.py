import numpy as np
import math

A, B = 5, 5  # 0<A<=B 
C = np.abs(A-B)/np.sqrt(4*A*B) # phi
H = 0.2 # Bump function

RANGE = 12
DISTANCE = 10

R = RANGE
D = DISTANCE

EPSILON = 0.1

def bump_function(z):
    Ph = np.zeros_like(z)
    Ph[z<=1] = (1 + np.cos(np.pi*(z[z<=1]-H)/(1-H)))/2
    Ph[z<H] = 1
    Ph[z<0] = 0
    # if 0 <= z < H:
    #     Ph = 1
    # elif H <= z <= 1:
    #     Ph = (1 + np.cos(np.pi*(z-H)/(1-H)))/2
    # else:
    #     Ph = 0
    return Ph

def phi(z):
    phi_val = ((A + B) * sigma_1(z+C) + (A-B)) / 2
    return phi_val

def phi_alpha(z):
    r_alpha = sigma_norm([R])
    d_alpha = sigma_norm([D])
    phi_alpha_val = bump_function(z/r_alpha) * phi(z-d_alpha)
    return phi_alpha_val

def sigma_1(z):
    sigma_1_val = z/np.sqrt(1 + z**2)
    return sigma_1_val

def sigma_norm(z):
    sigma_norm_val = (np.sqrt(1+EPSILON*np.linalg.norm(z, axis=-1, keepdims=True)**2)-1) / EPSILON 
    return sigma_norm_val

def sigma_grad(z):
    sigma_grad_val = z/np.sqrt(1 + EPSILON*np.linalg.norm(z, axis=-1, keepdims=True)**2)
    return sigma_grad_val

def get_adjacency_matrix(nodes, r):
    return np.array([np.linalg.norm(nodes[i,:2]-nodes[:,:2], axis=-1)<=r for i in range(len(nodes))])

def get_a_ij(q_i, q_js):
    r_alpha = sigma_norm([R])
    a_ij = bump_function(sigma_norm(q_js-q_i)/r_alpha)
    return a_ij

def get_n_ij(q_i, q_js):
    n_ij = sigma_grad(q_js-q_i)
    return n_ij