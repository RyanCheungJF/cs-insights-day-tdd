from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


@dataclass
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

    def navigate(self, steps: list[Step]):
        raise Exception
