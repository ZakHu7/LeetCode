from typing import Collection, List
from collections import deque
class Course:
  def __init__(self):
    self.children = set()
    self.count = 0

class Solution:
  def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    courses = [None] * numCourses
    for i in range(numCourses):
      courses[i] = Course()
      
    coursesBegin = [True] * numCourses
    for prerequisite in prerequisites:
      courses[prerequisite[1]].children.add(courses[prerequisite[0]])
      courses[prerequisite[0]].count += 1
      coursesBegin[prerequisite[0]] = False
    
    queue = deque()
    for i in range(numCourses):
      if coursesBegin[i]:
        queue.append(courses[i])
        
    while queue:
      course = queue.popleft()
      numCourses -= 1
      for child in course.children:
        child.count -= 1
        if child.count == 0:
          queue.append(child)
    return numCourses == 0
      