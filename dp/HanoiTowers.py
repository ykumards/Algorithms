"""
Given three towers and n sorted disks placed on it, we
have to move all the disks from one tower to the other
while using the third one as buffer.
There are three rules that each move should follow.
"""

def move(start, buffr, end, n):
    """
    By using the recursion from base case to move upwards
    we can change the roles of each of the three towers.
    The base case will be moving one disk from start to end.
    This can be done without any buffer, in one step.
    The behaviour of the function is modified by what type
    of the three stacks we send into it.
    """
    if n < 2:
        x = start.pop()
        return end.append(x)
    top = start.pop()
    buffr = move(start, end, buffr, n-1)
    
