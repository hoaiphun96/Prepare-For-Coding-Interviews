"""
You are given a data structure of employee information, which includes the employee's unique id, his importance value and his direct subordinates' id.

For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3. They have importance value 15, 10 and 5, respectively. Then employee 1 has a data structure like [1, 15, [2]], and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []]. Note that although employee 3 is also a subordinate of employee 1, the relationship is not direct.

Now given the employee information of a company, and an employee id, you need to return the total importance value of this employee and all his subordinates.

Example 1:
Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
Output: 11
Explanation:
Employee 1 has importance value 5, and he has two direct subordinates: employee 2 and employee 3. They both have importance value 3. So the total importance value of employee 1 is 5 + 3 + 3 = 11.
Note:
One employee has at most one direct leader and may have several subordinates.
The maximum number of employees won't exceed 2000.
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""


class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        has_seen_dict = {}
        subordinate = list()
        sum = 0
        foundBoss = False
        for e in employees:
            if e.id != id:
                has_seen_dict[e.id] = [e.importance, e.subordinates]
                if foundBoss:  # if seen boss, if subordinate contains(e), add sum
                    if e.id in subordinate:
                        subordinate += e.subordinates
                        sum += e.importance
                        subordinate.remove(e.id)
            else:  # if found target
                foundBoss = True
                sum += e.importance
                # add subordinates of this employees to the target's subordinate list
                subordinate += e.subordinates
                """
                :add all the subordinates' importance value to the return importance value, add this 
                subordinate's subordinates to the target subordinate list and remove the subordinate
                from the list after
                """
                for s in subordinate:
                    if s in has_seen_dict:
                        sum += has_seen_dict[s][0]
                        subordinate += has_seen_dict[s][1]
                        subordinate.remove(s)
                        # add the left over subordinates
        while len(subordinate) > 0:
            sleftover = subordinate[0]
            sum += has_seen_dict[sleftover][0]
            subordinate.remove(sleftover)
            subordinate += has_seen_dict[sleftover][1]
        return sum
