from abc import ABC, abstractmethod

# abstract base class for mesher
# all mesher classes should inherit from this class
# and implement the abstract methods
# this class is used to enforce the implementation of the methods
# and to provide a common interface for all mesher classes

class Mesher:
    @abstractmethod
    def load_points(self):
        pass
    @abstractmethod
    def load_edges(self):
        pass
    @abstractmethod
    def load_edge_radius(self):
        pass
    @abstractmethod
    def generate_mesh(self):
        pass
    @abstractmethod
    def save_mesh(self):
        pass
