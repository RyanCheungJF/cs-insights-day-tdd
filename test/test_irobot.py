import unittest
from unittest import TestCase

from insights.irobot import Heading, IRobot, Point, Step


class Test(TestCase):
    def test_move_forward(self):
        robot = IRobot(targets={}, heading=Heading.North, position=Point(0, 1))
        robot.navigate([Step.Forward])
        self.assertEqual(Heading.North, robot.heading)
        self.assertEqual(Point(0, 0), robot.position)

    @unittest.skip
    def test_move_backward(self):
        robot = IRobot(targets={}, heading=Heading.South, position=Point(0, 1))
        robot.navigate([Step.Backward])
        self.assertEqual(Heading.South, robot.heading)
        self.assertEqual(Point(0, 0), robot.position)

    @unittest.skip
    def test_rotate_left(self):
        robot = IRobot(targets={}, heading=Heading.East, position=Point(0, 0))
        robot.navigate([Step.Rotate_Left])
        self.assertEqual(Heading.North, robot.heading)
        self.assertEqual(Point(0, 0), robot.position)

    @unittest.skip
    def test_rotate_right(self):
        robot = IRobot(targets={}, heading=Heading.East, position=Point(0, 0))
        robot.navigate([Step.Rotate_Right])
        self.assertEqual(Heading.South, robot.heading)
        self.assertEqual(Point(0, 0), robot.position)

    @unittest.skip
    def test_can_go_forward(self):
        robot = IRobot(targets={Point(0, 0): '*', Point(1, 0): 'a'}, heading=Heading.North, position=Point(0, 1))
        self.assertEqual([
            Step.Forward
        ], robot >> '*')

    @unittest.skip
    def test_can_go_backward(self):
        robot = IRobot(targets={Point(0, 0): '*', Point(1, 0): 'a'}, heading=Heading.East, position=Point(1, 0))
        self.assertEqual([
            Step.Backward
        ], robot >> '*')

    @unittest.skip
    def test_can_go_left(self):
        robot = IRobot(targets={Point(0, 0): '*', Point(1, 0): 'a'}, heading=Heading.North, position=Point(1, 0))
        self.assertEqual([
            Step.Rotate_Left, Step.Forward
        ], robot >> '*')

    @unittest.skip
    def test_can_go_right(self):
        robot = IRobot(targets={Point(0, 0): '*', Point(1, 0): 'a'}, heading=Heading.North, position=Point(0, 0))
        self.assertEqual([
            Step.Rotate_Right, Step.Forward
        ], robot >> 'a')

    @unittest.skip
    def test_can_navigate(self):
        robot = IRobot(targets={Point(0, 0): '*', Point(2, 0): 'a'}, heading=Heading.East, position=Point(0, 0))
        robot.navigate(robot >> 'a')
        self.assertEqual(Heading.East, robot.heading)
        self.assertEqual(Point(2, 0), robot.position)

    @unittest.skip
    def test_unreachable(self):
        targets = {
            Point(0, 0): 'a',
            Point(2, 1): '#',
            Point(1, 2): '#',
            Point(3, 2): '#',
            Point(2, 3): '#',
        }
        robot = IRobot(targets=targets, heading=Heading.North, position=Point(2, 2))
        self.assertRaises(Exception, robot.__rshift__, 'a')
