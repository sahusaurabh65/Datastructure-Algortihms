
"""Defination of simple Vector class """
class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self,d):
        ''' Create d-dimensional vector of zeros'''
        self.coords = [0]*d

    def __len__(self):
        ''' Return the dimension of the vector. '''
        self.len(self.coords)

    def getitem(self, j):
        """Set jth coordinate of vector"""
        self.coords[j] = j

    def __setitem__(self,val):
        """Set jth coordinate of vector to given value."""

    def add(self, other):
        """Return sum of two vectors. """
        if len(self)!=len(other):                      # relies on __len__ method
            raise ValueError("Dimension are not matching")
        result = Vector(len(self))                     # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j]+other[j]
        return result

    def __eq__(self, other):
        """Return True if vector has same coordinates as other"""
        return self.coords == other.coords

    def __ne__(self, other):
        """Return True if vector differs from other."""
        return not self == other
