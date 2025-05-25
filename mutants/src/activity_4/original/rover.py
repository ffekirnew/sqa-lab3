from enum import StrEnum
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


class Direction(StrEnum):
    NORTH = "N"
    EAST = "E"
    SOUTH = "S"
    WEST = "W"


class Rover:
    def xǁRoverǁ__init____mutmut_orig(self, direction: Direction) -> None:
        self._direction = direction
    def xǁRoverǁ__init____mutmut_1(self, direction: Direction) -> None:
        self._direction = None
    
    xǁRoverǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁRoverǁ__init____mutmut_1': xǁRoverǁ__init____mutmut_1
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁRoverǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁRoverǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁRoverǁ__init____mutmut_orig)
    xǁRoverǁ__init____mutmut_orig.__name__ = 'xǁRoverǁ__init__'

    def xǁRoverǁturn_left__mutmut_orig(self) -> None:
        if self._direction == Direction.NORTH:
            self._direction = Direction.WEST
        elif self._direction == Direction.WEST:
            self._direction = Direction.SOUTH
        elif self._direction == Direction.SOUTH:
            self._direction = Direction.EAST
        else:
            self._direction = Direction.NORTH

    def xǁRoverǁturn_left__mutmut_1(self) -> None:
        if self._direction != Direction.NORTH:
            self._direction = Direction.WEST
        elif self._direction == Direction.WEST:
            self._direction = Direction.SOUTH
        elif self._direction == Direction.SOUTH:
            self._direction = Direction.EAST
        else:
            self._direction = Direction.NORTH

    def xǁRoverǁturn_left__mutmut_2(self) -> None:
        if self._direction == Direction.NORTH:
            self._direction = None
        elif self._direction == Direction.WEST:
            self._direction = Direction.SOUTH
        elif self._direction == Direction.SOUTH:
            self._direction = Direction.EAST
        else:
            self._direction = Direction.NORTH

    def xǁRoverǁturn_left__mutmut_3(self) -> None:
        if self._direction == Direction.NORTH:
            self._direction = Direction.WEST
        elif self._direction != Direction.WEST:
            self._direction = Direction.SOUTH
        elif self._direction == Direction.SOUTH:
            self._direction = Direction.EAST
        else:
            self._direction = Direction.NORTH

    def xǁRoverǁturn_left__mutmut_4(self) -> None:
        if self._direction == Direction.NORTH:
            self._direction = Direction.WEST
        elif self._direction == Direction.WEST:
            self._direction = None
        elif self._direction == Direction.SOUTH:
            self._direction = Direction.EAST
        else:
            self._direction = Direction.NORTH

    def xǁRoverǁturn_left__mutmut_5(self) -> None:
        if self._direction == Direction.NORTH:
            self._direction = Direction.WEST
        elif self._direction == Direction.WEST:
            self._direction = Direction.SOUTH
        elif self._direction != Direction.SOUTH:
            self._direction = Direction.EAST
        else:
            self._direction = Direction.NORTH

    def xǁRoverǁturn_left__mutmut_6(self) -> None:
        if self._direction == Direction.NORTH:
            self._direction = Direction.WEST
        elif self._direction == Direction.WEST:
            self._direction = Direction.SOUTH
        elif self._direction == Direction.SOUTH:
            self._direction = None
        else:
            self._direction = Direction.NORTH

    def xǁRoverǁturn_left__mutmut_7(self) -> None:
        if self._direction == Direction.NORTH:
            self._direction = Direction.WEST
        elif self._direction == Direction.WEST:
            self._direction = Direction.SOUTH
        elif self._direction == Direction.SOUTH:
            self._direction = Direction.EAST
        else:
            self._direction = None
    
    xǁRoverǁturn_left__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁRoverǁturn_left__mutmut_1': xǁRoverǁturn_left__mutmut_1, 
        'xǁRoverǁturn_left__mutmut_2': xǁRoverǁturn_left__mutmut_2, 
        'xǁRoverǁturn_left__mutmut_3': xǁRoverǁturn_left__mutmut_3, 
        'xǁRoverǁturn_left__mutmut_4': xǁRoverǁturn_left__mutmut_4, 
        'xǁRoverǁturn_left__mutmut_5': xǁRoverǁturn_left__mutmut_5, 
        'xǁRoverǁturn_left__mutmut_6': xǁRoverǁturn_left__mutmut_6, 
        'xǁRoverǁturn_left__mutmut_7': xǁRoverǁturn_left__mutmut_7
    }
    
    def turn_left(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁRoverǁturn_left__mutmut_orig"), object.__getattribute__(self, "xǁRoverǁturn_left__mutmut_mutants"), args, kwargs, self)
        return result 
    
    turn_left.__signature__ = _mutmut_signature(xǁRoverǁturn_left__mutmut_orig)
    xǁRoverǁturn_left__mutmut_orig.__name__ = 'xǁRoverǁturn_left'

    def xǁRoverǁturn_right__mutmut_orig(self) -> None:
        if self._direction == Direction.NORTH:
            self._direction = Direction.EAST
        elif self._direction == Direction.EAST:
            self._direction = Direction.SOUTH
        elif self._direction == Direction.SOUTH:
            self._direction = Direction.WEST
        else:
            self._direction = Direction.NORTH

    def xǁRoverǁturn_right__mutmut_1(self) -> None:
        if self._direction != Direction.NORTH:
            self._direction = Direction.EAST
        elif self._direction == Direction.EAST:
            self._direction = Direction.SOUTH
        elif self._direction == Direction.SOUTH:
            self._direction = Direction.WEST
        else:
            self._direction = Direction.NORTH

    def xǁRoverǁturn_right__mutmut_2(self) -> None:
        if self._direction == Direction.NORTH:
            self._direction = None
        elif self._direction == Direction.EAST:
            self._direction = Direction.SOUTH
        elif self._direction == Direction.SOUTH:
            self._direction = Direction.WEST
        else:
            self._direction = Direction.NORTH

    def xǁRoverǁturn_right__mutmut_3(self) -> None:
        if self._direction == Direction.NORTH:
            self._direction = Direction.EAST
        elif self._direction != Direction.EAST:
            self._direction = Direction.SOUTH
        elif self._direction == Direction.SOUTH:
            self._direction = Direction.WEST
        else:
            self._direction = Direction.NORTH

    def xǁRoverǁturn_right__mutmut_4(self) -> None:
        if self._direction == Direction.NORTH:
            self._direction = Direction.EAST
        elif self._direction == Direction.EAST:
            self._direction = None
        elif self._direction == Direction.SOUTH:
            self._direction = Direction.WEST
        else:
            self._direction = Direction.NORTH

    def xǁRoverǁturn_right__mutmut_5(self) -> None:
        if self._direction == Direction.NORTH:
            self._direction = Direction.EAST
        elif self._direction == Direction.EAST:
            self._direction = Direction.SOUTH
        elif self._direction != Direction.SOUTH:
            self._direction = Direction.WEST
        else:
            self._direction = Direction.NORTH

    def xǁRoverǁturn_right__mutmut_6(self) -> None:
        if self._direction == Direction.NORTH:
            self._direction = Direction.EAST
        elif self._direction == Direction.EAST:
            self._direction = Direction.SOUTH
        elif self._direction == Direction.SOUTH:
            self._direction = None
        else:
            self._direction = Direction.NORTH

    def xǁRoverǁturn_right__mutmut_7(self) -> None:
        if self._direction == Direction.NORTH:
            self._direction = Direction.EAST
        elif self._direction == Direction.EAST:
            self._direction = Direction.SOUTH
        elif self._direction == Direction.SOUTH:
            self._direction = Direction.WEST
        else:
            self._direction = None
    
    xǁRoverǁturn_right__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁRoverǁturn_right__mutmut_1': xǁRoverǁturn_right__mutmut_1, 
        'xǁRoverǁturn_right__mutmut_2': xǁRoverǁturn_right__mutmut_2, 
        'xǁRoverǁturn_right__mutmut_3': xǁRoverǁturn_right__mutmut_3, 
        'xǁRoverǁturn_right__mutmut_4': xǁRoverǁturn_right__mutmut_4, 
        'xǁRoverǁturn_right__mutmut_5': xǁRoverǁturn_right__mutmut_5, 
        'xǁRoverǁturn_right__mutmut_6': xǁRoverǁturn_right__mutmut_6, 
        'xǁRoverǁturn_right__mutmut_7': xǁRoverǁturn_right__mutmut_7
    }
    
    def turn_right(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁRoverǁturn_right__mutmut_orig"), object.__getattribute__(self, "xǁRoverǁturn_right__mutmut_mutants"), args, kwargs, self)
        return result 
    
    turn_right.__signature__ = _mutmut_signature(xǁRoverǁturn_right__mutmut_orig)
    xǁRoverǁturn_right__mutmut_orig.__name__ = 'xǁRoverǁturn_right'
