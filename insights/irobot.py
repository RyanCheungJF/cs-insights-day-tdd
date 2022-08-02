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

@dataclass
class IRobot:
    targets: dict[Point, str]
    heading: Heading
    position: Point

    def __rshift__(self, target: str) -> list[Step]:
        raise Exception
    
    def moveBot(self, dir: int) -> Point:
        if self.heading == Heading.North:
            self.position = Point(self.position.x, self.position.y - (dir * 1))
        elif self.heading == Heading.South:
            self.position = Point(self.position.x, self.position.y + (dir * 1))
        elif self.heading == Heading.East:
            self.position = Point(self.position.x + (dir * 1), self.position.y)
        elif self.heading == Heading.West:
            self.position = Point(self.position.x - (dir * 1), self.position.y)
        else:
            raise Exception

    def navigate(self, steps: list[Step]):
        for step in steps:
            if step == Step.Forward:
                self.moveBot(1)
            elif step == Step.Backward:
                self.moveBot(-1)
            else:
                raise Exception
