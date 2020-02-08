
import numpy as np
import matplotlib.pyplot as plt

def Parse():
    count = 0
    pointArray = []
    f = open("eigenCloudCSV.txt", "r+")
    for line in f:
        pointArray.append(line)
        count += 1

    f.close()

    xs = [None] * count
    ys = [None] * count

    for i in range(count):
        points = pointArray[i].split(", ")

        xs[i] = points[0]
        ys[i] = points[1]

        xs[i] = float(xs[i])
        ys[i] = float(ys[i])

    ##for i in range(count): 
    ##    xs[i] = float(xs[i])
    ##    ys[i] = float(ys[i])

    ##print(xs)
    ##print(ys)

    plt.plot(xs, ys, "bo")
    plt.show()

