points2D = [(1, 2), (3, 6), (8, 9), (2, 10)]

# sort by sum of each points
points2D_sorted = sorted(points2D, key=lambda x: x[0] + x[1])

print(points2D_sorted)
