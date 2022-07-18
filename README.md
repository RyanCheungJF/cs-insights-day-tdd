# Insights Day 2022

## TDD Demo

Given a number representing the calendar month-of-year (1 for January till 12 for December), return the calendar
quarter-of-year the month is in.

### Outputs

````text
 1 -> Q1
 2 -> Q1
 3 -> Q1
 4 -> Q2
 5 -> Q2
 6 -> Q2
 7 -> Q3
 8 -> Q3
 9 -> Q3
10 -> Q4
11 -> Q4
12 -> Q4
````

## Hands-on Exercise

A robotic waiter that can navigate the restaurant layout as a grid, starting with `(0, 0)` in the top-left corner.

    0123...
    1
    2*
    3   ^
    . North
    .
    .

It knows of:

* The kitchen and tables as a map of points; these are otherwise obstacles if not the target.
* current heading: `North/South/East/West`.
* current position `(x, y)`, e.g. `(1, 2)` refers to the `*` position in the above grid.

It can make the following steps:

* `Forward`: Goes forward by one position in the current heading, maintaining the same heading.
* `Backward`: Goes backward by one position in the current heading, maintaining the same heading.
* `Rotate_Left`: Turns left relative to the current heading, maintaining the same position.
* `Rotate_Right`: Turns right relative to the current heading, maintaining the same position.

Importantly, diagonal steps are not allowed.

It should have the following functions:

1. Given a target (kitchen or table), it can plot a list of steps to go there, without physically moving.
2. Given a list of steps, it will physically move there.
