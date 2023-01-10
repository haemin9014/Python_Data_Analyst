def Integer_Math(Side, Radius):
    AreaOfSquare = Side * Side;
    VolumeOfCube = Side * Side * Side;
    AreaOfCircle = round(Radius * Radius * math.pi, 2);
    VolumeOfSphere = round((4/3)*math.pi*Radius*Radius*Radius,2);
    print("Area of Square is %s" %AreaOfSquare);
    print("Volume of Cube is %s" %VolumeOfCube);
    print("Area of Circle is %s" %AreaOfCircle);
    print("Volume of Sphere is %s" %VolumeOfSphere);

# __name__ == '__main__':
#     Side = int(input().strip())

#     Radius = int(input().strip())

#     Integer_Math(Side, Radius)