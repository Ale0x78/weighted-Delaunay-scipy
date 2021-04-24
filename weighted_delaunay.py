from scipy.spatial import ConvexHull, Delaunay
import numpy as np

class WeightedDelaunay():
  def __init__(self, points, weights):
    num, dim = np.shape(points)
    lifted = np.zeros((num,dim+1))
    for i in range(num):
      p = points[i,:]
      lifted[i,:] = np.append(p,np.sum(p**2) - weights[i]**2)
    pinf = np.append(np.zeros((1,dim)),1e10);
    lifted = np.vstack((lifted, pinf))
    hull = ConvexHull(lifted)
    delaunay = []
    for simplex in hull.simplices:
        if num not in simplex:
            delaunay.append(simplex.tolist())
    self.triangulation = delaunay
    
  def addPoints(point, weight):
    pass

points = np.array([[3, 4], [5, 12], [10, 24], [24, 7], [12, 0]])
weights = [0,0,0,0,0]
d = WeightedDelaunay(points, weights).triangulation
d2 = Delaunay(points)
print(d) # returns [[1,4,0], [1,4,3], [1,2,3]]
print(d2.simplices.tolist()) # returns [[4,1,0], [1,4,3], [2,1,3]]
