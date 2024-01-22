'''
  Following on from 
  [Points of Reflection(https: www.codewars.com/kata/points-of-reflection),
  given a number of points and a single midpoint, a 2D shape can be inferred.

  Task:

  You will be given two inputs. The first will be a two-dimensional array in 
  which the inner arrays contain two elements representing partial coordinates of 
  a 2D shape. The second input will be a two-element array representing the shape's 
  mid-point. Using the existing coordinates and the mid-point, return the complete 
  shape as a two-dimensional array.'''

def symmetric_shape(shape, point):
    x0, y0 = point
    reflected_points = [[2 * x0 - x1, 2 * y0 - y1] for x1, y1 in shape]
    return shape + reflected_points

# Example Usage
original_shape = [[0, 0], [1, 1], [2, 0]]
point_of_symmetry = [1, 0]

symmetric = symmetric_shape(original_shape, point_of_symmetry)
print(symmetric)
# Output: [[0, 0], [1, 1], [2, 0], [2, 0], [1, -1], [0, 0]]
