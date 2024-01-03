from graphics import rectangle,circle
from graphics.threed import cuboid,sphere

#using rectangle module
length=5
width=3
print("Rectangle area:",rectangle.area(length,width))
print("rectangle perimeter :",rectangle.perimeter(length,width))

#using circle module
radius=4
print("circle area:",circle.area(radius))
print("circle perimeter:",circle.perimeter(radius))

#using cuboid module from 3d graphics 
length=3
width=5
height=8
print("Cuboid Surface Area:",cuboid.surface_area(length, width, height))
print("Cuboid Volume:",cuboid.volume(length, width,height))
