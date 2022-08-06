from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

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
    
    def moveBot(self, dir: int, x:int, y:int) -> Point:
        match self:
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

@dataclass
class IRobot:
    targets: dict[Point, str]
    heading: Heading
    position: Point

    def __rshift__(self, target: str) -> list[Step]:
        raise Exception

    def navigate(self, steps: list[Step]):
        for step in steps:
            if step == Step.Forward:
                self.position = self.heading.moveBot(1, self.position.x, self.position.y)
            elif step == Step.Backward:
                self.position = self.heading.moveBot(-1, self.position.x, self.position.y)
            elif step == Step.Rotate_Left or step == Step.Rotate_Right:
                self.heading = self.heading.changeDirection(step)
            else:
                raise Exception