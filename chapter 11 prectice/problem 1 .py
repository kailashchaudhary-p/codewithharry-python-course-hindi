#1. Create a class (2-D vector) and use it to create another class representing a 3-D vector.
class Vector2D:
    def __init__(self,x,y):
        self.x=y
        self.y=y
        class vector3D(Vector2D):
            def __init__(self,x,y,z):
                super().__init__(x,y)
                self.z=z
v3d=vector3D(1,2,3)
print(v3d.x,v3d.y,v3d.z)
