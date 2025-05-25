import pytest

from activity_4.original.rover import Direction, Rover


@pytest.fixture
def rover():
    """Fixture to create a Rover instance facing NORTH."""
    return Rover(Direction.NORTH)


def test_turn_left_from_north(rover):
    """Test turning left from NORTH."""
    rover.turn_left()
    assert rover._direction == Direction.WEST


def test_turn_left_from_west(rover):
    """Test turning left from WEST."""
    rover._direction = Direction.WEST
    rover.turn_left()
    assert rover._direction == Direction.SOUTH


def test_turn_left_from_south(rover):
    """Test turning left from SOUTH."""
    rover._direction = Direction.SOUTH
    rover.turn_left()
    assert rover._direction == Direction.EAST


def test_turn_left_from_east(rover):
    """Test turning left from EAST."""
    rover._direction = Direction.EAST
    rover.turn_left()
    assert rover._direction == Direction.NORTH


def test_turn_right_from_north(rover):
    """Test turning right from NORTH."""
    rover.turn_right()
    assert rover._direction == Direction.EAST


def test_turn_right_from_east(rover):
    """Test turning right from EAST."""
    rover._direction = Direction.EAST
    rover.turn_right()
    assert rover._direction == Direction.SOUTH


def test_turn_right_from_south(rover):
    """Test turning right from SOUTH."""
    rover._direction = Direction.SOUTH
    rover.turn_right()
    assert rover._direction == Direction.WEST


def test_turn_right_from_west(rover):
    """Test turning right from WEST."""
    rover._direction = Direction.WEST
    rover.turn_right()
    assert rover._direction == Direction.NORTH
