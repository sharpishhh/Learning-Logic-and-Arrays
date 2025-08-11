# Pythagorean Theorem
# In right triangle: Square of length of hypotenuse(side opp of right angle)
# is the sum of the squares of the lengths of the other two sides
# a^2 + b^2 = c^2

import math

def distance_two_pts(x1, y1, x2, y2):
    dist = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    return round(dist, 2)

if __name__ == '__main__':
    print(distance_two_pts(5, 5, 6, 6))