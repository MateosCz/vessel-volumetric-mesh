import pygel3d as pyg
import numpy as np
import matplotlib.pyplot as plt

# load numpy array
def load_array(filename):
    return np.load(filename)

# save numpy array
def save_array(filename, array):
    np.save(filename, array)

# generate a vertex radius from edge radius, input: edge indexed array, edge radius array, output: vertex radius array
def edge_radius_to_vertex_radius(edges, edge_radius):
    vertex_radius = np.zeros((edges.max()+1,))
    for i, edge in enumerate(edges):
        vertex_radius[edge[0]] = max(edge_radius[i], vertex_radius[edge[0]])     
        vertex_radius[edge[1]] = max(edge_radius[i], vertex_radius[edge[1]])
    return vertex_radius
