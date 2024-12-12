"""
Utility functions.
"""

from typing import Any, Callable, Iterable, List, Tuple, TypeVar

T = TypeVar("T")


def partition1(
    iterable: Iterable[T], pred: Callable[[T], bool], fun: Callable[[T], Any]
) -> Tuple[List[T], List[T]]:
    """
    Partitions iterable according to *pred.
    fun is applied to each element.
    """

    l0: List[T] = []
    other: List[T] = []
    for item in iterable:
        if pred(item):
            l0.append(fun(item))
        else:
            other.append(fun(item))
    return l0, other


def partition2(
    iterable: Iterable[T],
    pred0: Callable[[T], bool],
    pred1: Callable[[T], bool],
    fun: Callable[[T], Any],
) -> Tuple[List[T], List[T], List[T]]:
    """
    Partitions iterable according to *pred.
    fun is applied to each element.
    """

    l0: List[T] = []
    l1: List[T] = []
    other: List[T] = []
    for item in iterable:
        if pred0(item):
            l0.append(fun(item))
        elif pred1(item):
            l1.append(fun(item))
        else:
            other.append(fun(item))
    return l0, l1, other


def partition3(
    iterable: Iterable[T],
    pred0: Callable[[T], bool],
    pred1: Callable[[T], bool],
    pred2: Callable[[T], bool],
    fun: Callable[[T], Any],
) -> Tuple[List[T], List[T], List[T], List[T]]:
    """
    Partitions iterable according to *pred.
    fun is applied to each element.
    """

    l0: List[T] = []
    l1: List[T] = []
    l2: List[T] = []
    other: List[T] = []
    for item in iterable:
        if pred0(item):
            l0.append(fun(item))
        elif pred1(item):
            l1.append(fun(item))
        elif pred2(item):
            l2.append(fun(item))
        else:
            other.append(fun(item))
    return l0, l1, l2, other


def partition4(  # pylint: disable-msg=too-many-locals,too-many-positional-arguments
    iterable: Iterable[T],
    pred0: Callable[[T], bool],
    pred1: Callable[[T], bool],
    pred2: Callable[[T], bool],
    pred3: Callable[[T], bool],
    fun: Callable[[T], Any],
) -> Tuple[List[T], List[T], List[T], List[T], List[T]]:
    """
    Partitions iterable according to *pred.
    fun is applied to each element.
    """

    l0: List[T] = []
    l1: List[T] = []
    l2: List[T] = []
    l3: List[T] = []
    other: List[T] = []
    for item in iterable:
        if pred0(item):
            l0.append(fun(item))
        elif pred1(item):
            l1.append(fun(item))
        elif pred2(item):
            l2.append(fun(item))
        elif pred3(item):
            l3.append(fun(item))
        else:
            other.append(fun(item))
    return l0, l1, l2, l3, other


def partition(
    iterable: Iterable[T],
    *pred: Callable[[T], bool],
    fun: Callable[[T], Any] = lambda x: x
) -> Tuple[List[T], ...]:
    """
    Partitions iterable according to *pred.
    fun is applied to each element.
    """
    if len(pred) == 4:
        return partition4(iterable, pred[0], pred[1], pred[2], pred[3], fun)
    if len(pred) == 1:
        return partition1(iterable, pred[0], fun)
    if len(pred) == 2:
        return partition2(iterable, pred[0], pred[1], fun)
    if len(pred) == 3:
        return partition3(iterable, pred[0], pred[1], pred[2], fun)

    lists: Tuple[List[T], ...] = tuple([] for _ in range(len(pred) + 1))
    for item in iterable:
        added = False
        for i, p in enumerate(pred):
            if p(item):
                lists[i].append(fun(item))
                added = True
                break
        if not added:
            lists[-1].append(fun(item))
    return lists
