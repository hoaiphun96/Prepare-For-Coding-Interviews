"""

There are N students standing in a line where each student has some points.
You distribute chocolates to these students under the following constraints:

   1. Each student must have at least one chocolate.
   2. Students with a higher point value get more chocolates than their neighbors.

Write a method distributeChocolate to compute the minimum number of chocolates distributed
such that the above conditions are satisfied.

Example:

distributeChocolate("[1,5,7,1]") ==> 7

In this example, input is a list of points which 4 different students have been allotted.
The minimum number of chocolates distributed i.e. the output is 7.
"""


def distributeChocolate(points):
    if not points:
        return 0
    chocolate = [1]
    for index in range(1, len(points)):
        if points[index] > points[index - 1]:
            chocolate.append(chocolate[-1] + 1)
        else:
            chocolate.append(1)
    for index in range(len(points) - 2, 0, -1):
        if points[index] > points[index + 1]:
            chocolate[index] = max(chocolate[index], chocolate[index + 1] + 1)
    ret = 0
    for choco in chocolate:
        ret += choco
    return ret
