#Write a class vector representing a vector of n dimensions. Overload the + and * operator which calculates the sum and the dot(.) product of them.
class vector:
    def __init__(self, components):
        self.components = components

    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for addition.")
        return vector([a + b for a, b in zip(self.components, other.components)])

    def __mul__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for dot product.")
        return sum(a * b for a, b in zip(self.components, other.components))
#example usage
v1=vector([1,2,3])
v2=vector([4,5,6])
v3=v1+v2
print(v3.components)
dot_product=v1*v2
print(dot_product)