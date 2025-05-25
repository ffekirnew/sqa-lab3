from enum import StrEnum


class Direction(StrEnum):
    NORTH = "N"
    EAST = "E"
    SOUTH = "S"
    WEST = "W"


class Rover:
    def __init__(self, direction: Direction) -> None:
        self._direction = direction

    def turn_left(self) -> None:
        if self._direction == Direction.NORTH:
            self._direction = Direction.WEST
        elif self._direction == Direction.WEST:
            self._direction = Direction.SOUTH
        elif self._direction == Direction.SOUTH:
            self._direction = Direction.EAST
        elif self._direction == Direction.EAST:
            self._direction = Direction.NORTH

    def turn_right(self) -> None:
        if self._direction == Direction.NORTH:
            self._direction = Direction.EAST
        elif self._direction == Direction.EAST:
            self._direction = Direction.SOUTH
        elif self._direction == Direction.SOUTH:
            self._direction = Direction.WEST
        elif self._direction != Direction.WEST:
            self._direction = Direction.NORTH
