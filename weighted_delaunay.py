from scipy.spatial import ConvexHull, Delaunay

class WeightedDelaunay(Delaunay):
    def __init__(self, points, weights=[], furthest_site=False, incremental=False, qhull_options=None):
        super(points, furthest_site, incremental, qhull_options)

    # Process a set of additional new points.
    def add_points(self, points, restart=False):
        pass

    # Finish incremental processing.
    # MARK SAYS: This does not depend on weights. Can remove.
    def close(self):
        pass

    # Find the simplices containing the given points.
    # Need to look through weighted rather than 
    def find_simplex(self, xi, bruteforce=False, tol=None):
        pass
    # Lift points to the Qhull paraboloid.
    def lift_points(self, x):
        pass

    # Compute hyperplane distances to the point xi from all simplices.
    # MARK SAYS: This does not depend on weights. Can remove.
    def plane_distance(self, xi):
        pass

WeightedDelaunay()

#
# points  ndarray of double, shape (npoints, ndim)
# Coordinates of input points.
# simplices ndarray of ints, shape (nsimplex, ndim+1)
# Indices of the points forming the simplices in the triangulation. For 2-D, the points are oriented counterclockwise.
# neighbors ndarray of ints, shape (nsimplex, ndim+1)
# Indices of neighbor simplices for each simplex. The kth neighbor is opposite to the kth vertex. For simplices at the boundary, -1 denotes no neighbor.
# equations ndarray of double, shape (nsimplex, ndim+2)
# [normal, offset] forming the hyperplane equation of the facet on the paraboloid (see Qhull documentation for more).
# paraboloid_scale, paraboloid_shiftfloat
# Scale and shift for the extra paraboloid dimension (see Qhull documentation for more).
# transformndarray of double, shape (nsimplex, ndim+1, ndim)
# Affine transform from x to the barycentric coordinates c.
# vertex_to_simplexndarray of int, shape (npoints,)
# Lookup array, from a vertex, to some simplex which it is a part of.
# convex_hullndarray of int, shape (nfaces, ndim)
# Vertices of facets forming the convex hull of the point set.
# coplanarndarray of int, shape (ncoplanar, 3)
# Indices of coplanar points and the corresponding indices of the nearest facet and the nearest vertex. Coplanar points are input points which were not included in the triangulation due to numerical precision issues.
# If option “Qc” is not specified, this list is not computed.
# New in version 0.12.0.
# vertices
# Same as simplices, but deprecated.
# vertex_neighbor_verticestuple of two ndarrays of int; (indptr, indices)
# Neighboring vertices of vertices.
# furthest_site
# True if this was a furthest site triangulation and False if not.
# New in version 1.4.0.
