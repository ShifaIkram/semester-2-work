# Taking input
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Distance formula (Calculating distance b/w two points)
print("-------Distance Formula--------\n [(x2 - x1)^2 + (y2 - y1)^2)]^0.5")
distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

print("Distance between the points:", distance)

# Checking quadrant for point 1
if x1 > 0 and y1 > 0:
    print(f"Point 1 (",x1,",",y1,") is in First Quadrant")
elif x1 < 0 and y1 > 0:
    print(f"Point 1 (",x1,",",y1,") is in Second Quadrant")
elif x1 < 0 and y1 < 0:
    print(f"Point 1 (",x1,",",y1,") is in Third Quadrant")
elif x1 > 0 and y1 < 0:
    print(f"Point 1 (",x1,",",y1,") is in Fourth Quadrant")
elif x1 ==0 and y1 == 0:
    print(f"Point 1 (", x1,",",y1,") is on origin")
else:
    print(f"Point 1 (", x1, ",", y1, ") is on axis")


# Checking quadrant for point 2
if x2 > 0 and y2 > 0:
    print(f"Point 2 (",x2,",",y2,") is in First Quadrant")
elif x2 < 0 and y2 > 0:
    print(f"Point 2 (",x2,",",y2,") is in Second Quadrant")
elif x2 < 0 and y2 < 0:
    print(f"Point 2 (",x2,",",y2,") is in Third Quadrant")
elif x2 > 0 and y2 < 0:
    print(f"Point 2 (",x2,",",y2,") is in Fourth Quadrant")
elif x2==0 and y2==0:
    print(f"Point 2 (",x2,",",y2,") is on origin")
else:
    print(f"Point 2 (",x2,",",y2,") is on axis")
