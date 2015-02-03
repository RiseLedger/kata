import math

#Cylinder: V = math.pi r2h
#Sphere: V = 4/3 math.pi r3
#Cone: V = math.pi r2h / 3

volume = input()
side = math.pow( volume, 1.0/3 )
radius = math.sqrt( volume / ( math.pi * side ) )
diameter = radius * 2
sphere_radius = math.pow( (volume * 3) / (4 * math.pi), 1.0/3 )
tall = (3 * volume) / (math.pi * math.pow(radius, 2) )

print("Cube: %.2fm width, %.2fm, high, %.2fm tall" % (side, side, side) )
print("Cylinder: %.2fm tall, Diameter of %.2fm" % (side , diameter ) )
print("Sphere: %.2fm Radius" % sphere_radius)
print("Cone: %.2fm tall, %.2fm Radius" % (tall, radius))
