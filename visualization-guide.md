# Visualization Guide

To use our visualization, you will first need to run `visualization.py`.
This will pull up a black screen on which you can click and drag to create points for your weighted Delaunay.
You can also press the `u` key to remove points in order of how recently they were added.

Here is a step-by-step walkthrough, with figures, on what to expect from this visualization.

1. First, you can click anywhere to add one point to your set.

![One Point](/images/one_point.png)

2. When you add a second point, they will both appear with no edge between them.

![Two Points](/images/two_points.png)

3. When you add a third point, you will see a triangle form.

![Three Points](/images/three_points.png)

4. As you add even more points, the weighted Delaunay triangulation will recompute for each point, and the most up-to-date version will be displayed. If none of your points are particularly heavy, this looks like a regular Delaunay triangulation, shown below.

![Delaunay](/images/many_points.png)

5. When you add a heavy point (by clicking and dragging the mouse far before releasing), you can see how the weighted Delaunay triangulation appears different from how a regular one would.

![One Heavy Point](/images/one_heavy_point.png)

6. With another heavy point added, we can again see how the weighted Delaunay differs from the regular Delaunay triangulation for this set of points.

![Two Heavy Points](/images/two_heavy_points.png)
