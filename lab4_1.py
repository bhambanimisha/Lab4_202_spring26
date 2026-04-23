from dataclasses import dataclass
from array_code import ArrayList, append, delete, get


@dataclass
class ArrayStack:
    stack: ArrayList


def push(s: ArrayStack, n: int) -> ArrayStack:
    """
    Returns a new ArrayStack with n pushed onto the top.
    """
    if s.stack.next == s.stack.size:
        raise IndexError
    new_array: ArrayList = append(s.stack, n)
    return ArrayStack(new_array)



def pop(s: ArrayStack) -> tuple[int, ArrayStack]:
    """
    Returns a tuple (value, new_stack), where value is the top item
    that was removed.

    Raises IndexError if the stack is empty.
    """
    if s.stack.size == 0:
        raise IndexError
    top: int = s.stack.next-1
    v: int = s.stack.array[top]
    new_array: ArrayList = delete(s.stack, top)
    return (v, ArrayStack(new_array))

def peek(s: ArrayStack) -> int:
    """
    Returns the top value without removing it.

    Raises IndexError if the stack is empty.
    """ 
    if s.stack.size == 0:
        raise IndexError 
    return s.stack.array[s.stack.next-1]


def is_empty(s: ArrayStack) -> bool:
    """
    Returns True if the stack is empty, otherwise False.
    """
    return s.stack.next == 0