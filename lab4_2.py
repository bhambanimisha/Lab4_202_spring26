from dataclasses import dataclass
from array_code import ArrayList, append, delete, get


@dataclass
class ArrayQueue:
    queue: ArrayList


def enqueue(q: ArrayQueue, n: int) -> ArrayQueue:
    """
    Returns a new ArrayQueue with n added to the back.
    """
    if q.queue.next == q.queue.size:
        raise OverflowError
    new_array = append(q.queue, n)
    return ArrayQueue(new_array)


def dequeue(q: ArrayQueue) -> tuple[int, ArrayQueue]:
    """
    Returns a tuple (value, new_queue), where value is the
    front item that was removed.

    Raises IndexError if the queue is empty.
    """
    if q.queue.next == 0:
        raise IndexError
    value:int = q.queue.array[0]
    new_array = delete(q.queue, 0)
    return value, ArrayQueue(new_array)


def peek(q: ArrayQueue) -> int:
    """
    Returns the front value without removing it.

    Raises IndexError if the queue is empty.
    """
    if q.queue.next == 0:
        raise IndexError
    return q.queue.array[0]


def is_empty(q: ArrayQueue) -> bool:
    """
    Returns True if the queue is empty, otherwise False.
    """
    return q.queue.next == 0

def resize(q:ArrayQueue, f:int) -> ArrayQueue:
    new_size = q.queue.size*f
    new_queue = ArrayQueue(Array(new_size, [None]*new_size, 0))
    for i in range(q.queue.next):
        v,q = dequeue(q)
        new_queue = enqueue(new_queue, v)
    return new_queue