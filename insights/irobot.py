from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from heapq import heapify, heappop, heappush

"""
@dataclass
A class but automatically generates init (constructor) and repr (toString)
frozen makes class immutable
"""

@dataclass(frozen=True)
class Point:
    x: int
    y: int

class Step(Enum):
    Forward = 'Forward'
    Backward = 'Backward'
    Rotate_Left = 'Rotate Left'
    Rotate_Right = 'Rotate Right'

class Heading(Enum):
    North = 'North'
    South = 'South'
    East = 'East'
    West = 'West'
    
    def moveBot(self, hd: Heading, dir: int, x: int, y: int) -> Point:
        match hd:
            case Heading.North:
                return Point(x, y - (dir * 1))
            case Heading.South:
                return Point(x, y + (dir * 1))
            case Heading.East:
                return Point(x + (dir * 1), y)
            case Heading.West:
                return Point(x - (dir * 1), y)
            case _:
                raise Exception
    
    def changeDirection(self, step: Step) -> Heading:
        match (self, step):
            case (Heading.North, Step.Rotate_Left) | (Heading.South, Step.Rotate_Right):
                return Heading.West
            case (Heading.South, Step.Rotate_Left) | (Heading.North, Step.Rotate_Right):
                return Heading.East
            case (Heading.East, Step.Rotate_Left) | (Heading.West, Step.Rotate_Right):
                return Heading.North
            case (Heading.West, Step.Rotate_Left) | (Heading.East, Step.Rotate_Right):
                return Heading.South
            case _:
                raise Exception
            
    def generateNextStep(self, soln: Solution) -> list[Solution]:
        # head up
        up = Solution(
            soln.heading, 
            self.moveBot(soln.heading, 1, soln.position.x, soln.position.y), 
            soln.steps + [Step.Forward]
        )
        # head down
        down = Solution(
            soln.heading, 
            self.moveBot(soln.heading, -1, soln.position.x, soln.position.y), 
            soln.steps + [Step.Backward]
        )
        # head left
        newDir = self.changeDirection(Step.Rotate_Left)
        left = Solution(
            newDir, 
            self.moveBot(newDir, 1, soln.position.x, soln.position.y), 
            soln.steps + [Step.Rotate_Left, Step.Forward]
        )
        # head right
        newDir = self.changeDirection(Step.Rotate_Right)
        right = Solution(
            newDir, 
            self.moveBot(newDir, 1, soln.position.x, soln.position.y), 
            soln.steps + [Step.Rotate_Right, Step.Forward]
        )
        return [up, down, left, right]
            
@dataclass
class Solution:
    heading: Heading
    position: Point
    steps: list[Step]
    
    # __{name}__ is for dunder methods
    
    # override < property, used for heap comparison
    def __lt__(self, other: Solution) -> bool:
        return self.cost < other.cost

    # provides getter, setter, deleter
    @property
    def cost(self) -> int:
        return len(self.steps)

@dataclass
class IRobot:
    targets: dict[Point, str]
    heading: Heading
    position: Point

    """
    denoted with right shift for >> method call
    """
    def __rshift__(self, target: str) -> list[Step]:
        # exceptional cases: if test case has no targets
        if len(self.targets) == 0 or target not in self.targets.values():
            raise Exception
        
        # keeps track of what nodes have been visited
        visited = set()
        visited.add(self.position)
        
        # start dfs from curr pos, we use heapify to get type system
        minHeap = [Solution(self.heading, self.position, [])]
        heapify(minHeap)
        
        # continue our path finding till we run out of new nodes to explore
        while minHeap:
            curr = heappop(minHeap)
            
            # if we get to the target, just return the list of steps
            if self.targets.get(curr.position) == target:
                return curr.steps
            
            # if not, let us prepare the next few steps
            nextSteps = curr.heading.generateNextStep(curr)
            for step in nextSteps:
                if step.position not in visited:
                    visited.add(step.position)
                    heappush(minHeap, step)

        # if no path found, there must exist an error
        raise Exception

    def navigate(self, steps: list[Step]):
        for step in steps:
            if step == Step.Forward:
                self.position = self.heading.moveBot(self.heading, 1, self.position.x, self.position.y)
            elif step == Step.Backward:
                self.position = self.heading.moveBot(self.heading, -1, self.position.x, self.position.y)
            elif step == Step.Rotate_Left or step == Step.Rotate_Right:
                self.heading = self.heading.changeDirection(step)
            else:
                raise Exception