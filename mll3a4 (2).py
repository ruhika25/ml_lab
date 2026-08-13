# minkowski distance

def mink_dist(x, y, p):
    s = 0
    for i in range(len(x)):
        s += abs(x[i] - y[i])**p
    return s**(1/p)
a=[2, 4, 6]
b=[5, 8, 10]

print("Manhattan:",mink_dist(a, b, 1))
print("Euclidean:",mink_dist(a, b, 2))