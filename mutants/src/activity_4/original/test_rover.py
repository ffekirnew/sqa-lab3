import pytest

from activity_4.original.rover import Direction, Rover
from inspect import signature as _mutmut_signature
from typing import Annotated
from typing import Callable
from typing import ClassVar


MutantDict = Annotated[dict[str, Callable], "Mutant"]


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None):
    """Forward call to original or mutated function, depending on the environment"""
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*call_args, **call_kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*call_args, **call_kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    if self_arg:
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs)
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs)
    return result
from inspect import signature as _mutmut_signature
from typing import Annotated
from typing import Callable
from typing import ClassVar


MutantDict = Annotated[dict[str, Callable], "Mutant"]


def _mutmut_yield_from_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None):
    """Forward call to original or mutated function, depending on the environment"""
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*call_args, **call_kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*call_args, **call_kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    if self_arg:
        # call to a class method where self is not bound
        result = yield from mutants[mutant_name](self_arg, *call_args, **call_kwargs)
    else:
        result = yield from mutants[mutant_name](*call_args, **call_kwargs)
    return result


@pytest.fixture
def rover():
    """Fixture to create a Rover instance facing NORTH."""
    return Rover(Direction.NORTH)


def x_test_turn_left_from_north__mutmut_orig(rover):
    """Test turning left from NORTH."""
    rover.turn_left()
    assert rover._direction == Direction.WEST


def x_test_turn_left_from_north__mutmut_1(rover):
    """Test turning left from NORTH."""
    rover.turn_left()
    assert rover._direction != Direction.WEST

x_test_turn_left_from_north__mutmut_mutants : ClassVar[MutantDict] = {
'x_test_turn_left_from_north__mutmut_1': x_test_turn_left_from_north__mutmut_1
}

def test_turn_left_from_north(*args, **kwargs):
    result = _mutmut_trampoline(x_test_turn_left_from_north__mutmut_orig, x_test_turn_left_from_north__mutmut_mutants, args, kwargs)
    return result 

test_turn_left_from_north.__signature__ = _mutmut_signature(x_test_turn_left_from_north__mutmut_orig)
x_test_turn_left_from_north__mutmut_orig.__name__ = 'x_test_turn_left_from_north'


def x_test_turn_left_from_west__mutmut_orig(rover):
    """Test turning left from WEST."""
    rover._direction = Direction.WEST
    rover.turn_left()
    assert rover._direction == Direction.SOUTH


def x_test_turn_left_from_west__mutmut_1(rover):
    """Test turning left from WEST."""
    rover._direction = None
    rover.turn_left()
    assert rover._direction == Direction.SOUTH


def x_test_turn_left_from_west__mutmut_2(rover):
    """Test turning left from WEST."""
    rover._direction = Direction.WEST
    rover.turn_left()
    assert rover._direction != Direction.SOUTH

x_test_turn_left_from_west__mutmut_mutants : ClassVar[MutantDict] = {
'x_test_turn_left_from_west__mutmut_1': x_test_turn_left_from_west__mutmut_1, 
    'x_test_turn_left_from_west__mutmut_2': x_test_turn_left_from_west__mutmut_2
}

def test_turn_left_from_west(*args, **kwargs):
    result = _mutmut_trampoline(x_test_turn_left_from_west__mutmut_orig, x_test_turn_left_from_west__mutmut_mutants, args, kwargs)
    return result 

test_turn_left_from_west.__signature__ = _mutmut_signature(x_test_turn_left_from_west__mutmut_orig)
x_test_turn_left_from_west__mutmut_orig.__name__ = 'x_test_turn_left_from_west'


def x_test_turn_left_from_south__mutmut_orig(rover):
    """Test turning left from SOUTH."""
    rover._direction = Direction.SOUTH
    rover.turn_left()
    assert rover._direction == Direction.EAST


def x_test_turn_left_from_south__mutmut_1(rover):
    """Test turning left from SOUTH."""
    rover._direction = None
    rover.turn_left()
    assert rover._direction == Direction.EAST


def x_test_turn_left_from_south__mutmut_2(rover):
    """Test turning left from SOUTH."""
    rover._direction = Direction.SOUTH
    rover.turn_left()
    assert rover._direction != Direction.EAST

x_test_turn_left_from_south__mutmut_mutants : ClassVar[MutantDict] = {
'x_test_turn_left_from_south__mutmut_1': x_test_turn_left_from_south__mutmut_1, 
    'x_test_turn_left_from_south__mutmut_2': x_test_turn_left_from_south__mutmut_2
}

def test_turn_left_from_south(*args, **kwargs):
    result = _mutmut_trampoline(x_test_turn_left_from_south__mutmut_orig, x_test_turn_left_from_south__mutmut_mutants, args, kwargs)
    return result 

test_turn_left_from_south.__signature__ = _mutmut_signature(x_test_turn_left_from_south__mutmut_orig)
x_test_turn_left_from_south__mutmut_orig.__name__ = 'x_test_turn_left_from_south'


def x_test_turn_left_from_east__mutmut_orig(rover):
    """Test turning left from EAST."""
    rover._direction = Direction.EAST
    rover.turn_left()
    assert rover._direction == Direction.NORTH


def x_test_turn_left_from_east__mutmut_1(rover):
    """Test turning left from EAST."""
    rover._direction = None
    rover.turn_left()
    assert rover._direction == Direction.NORTH


def x_test_turn_left_from_east__mutmut_2(rover):
    """Test turning left from EAST."""
    rover._direction = Direction.EAST
    rover.turn_left()
    assert rover._direction != Direction.NORTH

x_test_turn_left_from_east__mutmut_mutants : ClassVar[MutantDict] = {
'x_test_turn_left_from_east__mutmut_1': x_test_turn_left_from_east__mutmut_1, 
    'x_test_turn_left_from_east__mutmut_2': x_test_turn_left_from_east__mutmut_2
}

def test_turn_left_from_east(*args, **kwargs):
    result = _mutmut_trampoline(x_test_turn_left_from_east__mutmut_orig, x_test_turn_left_from_east__mutmut_mutants, args, kwargs)
    return result 

test_turn_left_from_east.__signature__ = _mutmut_signature(x_test_turn_left_from_east__mutmut_orig)
x_test_turn_left_from_east__mutmut_orig.__name__ = 'x_test_turn_left_from_east'


def x_test_turn_right_from_north__mutmut_orig(rover):
    """Test turning right from NORTH."""
    rover.turn_right()
    assert rover._direction == Direction.EAST


def x_test_turn_right_from_north__mutmut_1(rover):
    """Test turning right from NORTH."""
    rover.turn_right()
    assert rover._direction != Direction.EAST

x_test_turn_right_from_north__mutmut_mutants : ClassVar[MutantDict] = {
'x_test_turn_right_from_north__mutmut_1': x_test_turn_right_from_north__mutmut_1
}

def test_turn_right_from_north(*args, **kwargs):
    result = _mutmut_trampoline(x_test_turn_right_from_north__mutmut_orig, x_test_turn_right_from_north__mutmut_mutants, args, kwargs)
    return result 

test_turn_right_from_north.__signature__ = _mutmut_signature(x_test_turn_right_from_north__mutmut_orig)
x_test_turn_right_from_north__mutmut_orig.__name__ = 'x_test_turn_right_from_north'


def x_test_turn_right_from_east__mutmut_orig(rover):
    """Test turning right from EAST."""
    rover._direction = Direction.EAST
    rover.turn_right()
    assert rover._direction == Direction.SOUTH


def x_test_turn_right_from_east__mutmut_1(rover):
    """Test turning right from EAST."""
    rover._direction = None
    rover.turn_right()
    assert rover._direction == Direction.SOUTH


def x_test_turn_right_from_east__mutmut_2(rover):
    """Test turning right from EAST."""
    rover._direction = Direction.EAST
    rover.turn_right()
    assert rover._direction != Direction.SOUTH

x_test_turn_right_from_east__mutmut_mutants : ClassVar[MutantDict] = {
'x_test_turn_right_from_east__mutmut_1': x_test_turn_right_from_east__mutmut_1, 
    'x_test_turn_right_from_east__mutmut_2': x_test_turn_right_from_east__mutmut_2
}

def test_turn_right_from_east(*args, **kwargs):
    result = _mutmut_trampoline(x_test_turn_right_from_east__mutmut_orig, x_test_turn_right_from_east__mutmut_mutants, args, kwargs)
    return result 

test_turn_right_from_east.__signature__ = _mutmut_signature(x_test_turn_right_from_east__mutmut_orig)
x_test_turn_right_from_east__mutmut_orig.__name__ = 'x_test_turn_right_from_east'


def x_test_turn_right_from_south__mutmut_orig(rover):
    """Test turning right from SOUTH."""
    rover._direction = Direction.SOUTH
    rover.turn_right()
    assert rover._direction == Direction.WEST


def x_test_turn_right_from_south__mutmut_1(rover):
    """Test turning right from SOUTH."""
    rover._direction = None
    rover.turn_right()
    assert rover._direction == Direction.WEST


def x_test_turn_right_from_south__mutmut_2(rover):
    """Test turning right from SOUTH."""
    rover._direction = Direction.SOUTH
    rover.turn_right()
    assert rover._direction != Direction.WEST

x_test_turn_right_from_south__mutmut_mutants : ClassVar[MutantDict] = {
'x_test_turn_right_from_south__mutmut_1': x_test_turn_right_from_south__mutmut_1, 
    'x_test_turn_right_from_south__mutmut_2': x_test_turn_right_from_south__mutmut_2
}

def test_turn_right_from_south(*args, **kwargs):
    result = _mutmut_trampoline(x_test_turn_right_from_south__mutmut_orig, x_test_turn_right_from_south__mutmut_mutants, args, kwargs)
    return result 

test_turn_right_from_south.__signature__ = _mutmut_signature(x_test_turn_right_from_south__mutmut_orig)
x_test_turn_right_from_south__mutmut_orig.__name__ = 'x_test_turn_right_from_south'


def x_test_turn_right_from_west__mutmut_orig(rover):
    """Test turning right from WEST."""
    rover._direction = Direction.WEST
    rover.turn_right()
    assert rover._direction == Direction.NORTH


def x_test_turn_right_from_west__mutmut_1(rover):
    """Test turning right from WEST."""
    rover._direction = None
    rover.turn_right()
    assert rover._direction == Direction.NORTH


def x_test_turn_right_from_west__mutmut_2(rover):
    """Test turning right from WEST."""
    rover._direction = Direction.WEST
    rover.turn_right()
    assert rover._direction != Direction.NORTH

x_test_turn_right_from_west__mutmut_mutants : ClassVar[MutantDict] = {
'x_test_turn_right_from_west__mutmut_1': x_test_turn_right_from_west__mutmut_1, 
    'x_test_turn_right_from_west__mutmut_2': x_test_turn_right_from_west__mutmut_2
}

def test_turn_right_from_west(*args, **kwargs):
    result = _mutmut_trampoline(x_test_turn_right_from_west__mutmut_orig, x_test_turn_right_from_west__mutmut_mutants, args, kwargs)
    return result 

test_turn_right_from_west.__signature__ = _mutmut_signature(x_test_turn_right_from_west__mutmut_orig)
x_test_turn_right_from_west__mutmut_orig.__name__ = 'x_test_turn_right_from_west'
