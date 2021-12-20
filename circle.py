import math

radius = input("Radius:\n")
xo = input("X-coordinate of center:\n")
yo = input("Y-coordinate of center:\n")

x1 = input("X-coordinate of point A:\n")
y1 = input("Y-coordinate of point A:\n")

radius = int(radius)
xo = int(xo)
yo = int(yo)
y1 = int(y1)
x1 = int(x1)



Area = math.pi*math.pow(radius,2)
Perimeter = 2*math.pi*radius

dx = math.fabs(xo-x1)
dy = math.fabs(yo-y1)

distance = math.sqrt(math.pow(dx,2)+math.pow(dy,2))

if distance == radius:
    print("The point A is on the circle")
elif distance > radius:
    print("The point A is outside the circle")
else:
    print("The point A is inside the circle")

print("The Perimeter of the circle is:" + str(math.floor(Perimeter)))
print("The Area of the circle is:", math.ceil(Area))
print("The distance  between the circle and the point A is:", distance)

