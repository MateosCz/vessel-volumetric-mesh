import pyopenvdb as vdb
import numpy as np
import matplotlib.pyplot as plt
import Mesher

class Isocontour_Mesher(Mesher.Mesher):
    def __init__(self, grid=None, iso_value=None):
        self.grid = grid
        self.iso_value = iso_value
        self.points = []
        self.edges = []
        self.edge_radius = []
        self.mesh = None

    def load_points(self, filename):
        self.points = np.load(filename)

    def load_edges(self, filename):
        self.edges = np.load(filename)
    
    def load_edge_radius(self, filename):
        self.edge_radius = np.load(filename)
    
    def generate_mesh(self):
        