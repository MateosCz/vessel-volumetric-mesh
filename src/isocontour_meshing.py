import numpy as np
import matplotlib.pyplot as plt
import pygel3d as pyg
import sys
import os
import time
import mesh_util

# generate a mesh
def generate_mesh(vertices, edges, vertex_radius, edge_radius, iso_value, output_filename):
    # create mesh
    mesh = pyg.Mesh()
    # add vertices
    for vertex in vertices:
        mesh.add_vertex(vertex)
    # add edges
    for edge in edges:
        mesh.add_edge(edge[0], edge[1])
    # add faces
    mesh.add_faces_from_edges()
    # add vertex radius
    mesh.add_vertex_property("radius")
    for i, radius in enumerate(vertex_radius):
        mesh.set_vertex_property("radius", i, radius)
    # add edge radius
    mesh.add_edge_property("radius")
    for i, radius in enumerate(edge_radius):
        mesh.set_edge_property("radius", i, radius)
    # generate isocontour mesh
    isocontour_mesh = pyg.isocontour_mesh(mesh, iso_value)
    # save mesh
    isocontour_mesh.save(output_filename)

def main():
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

    # load numpy array
 
    vertices = load_array("data/points.npy")
    edges = load_array("data/edge_array.npy")
    edge_radius = load_array("data/edge_radius.npy")
    # generate vertex radius
    vertex_radius = edge_radius_to_vertex_radius(edges, edge_radius)
    # generate mesh
    generate_mesh(vertices, edges, vertex_radius, edge_radius, 0.5, "isocontour_mesh.off")

if __name__ == "__main__":
    main()