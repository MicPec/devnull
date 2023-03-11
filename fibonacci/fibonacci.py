#!/usr/bin/env python3

from functools import lru_cache
from timeit import timeit


def fib_iterative(n: int) -> int:
    """Fibonacci number using iteration"""
    if n < 2:
        return n
    fib1, fib2 = 1, 0
    for _ in range(n):
        fib1, fib2 = fib2, fib1 + fib2
    return fib2


def fib_recursive(n: int) -> int:
    """Fibonacci number using recursion"""
    if n < 2:
        return n
    return fib_recursive(n - 2) + fib_recursive(n - 1)


def fib_recursive_cached(n: int, cache: dict) -> int:
    """Fibonacci number using recursion and caching"""
    if n < 2:
        return n
    if n not in cache:
        cache[n] = fib_recursive_cached(n - 2, cache) + fib_recursive_cached(
            n - 1, cache
        )
    return cache[n]


def fib_recursive_cached_generator(n: int, cache: dict) -> int:
    """Fibonacci number using recursion, caching and generator"""
    if n < 2:
        yield n
    if n not in cache:
        cache[n] = fib_recursive_cached_generator(
            n - 2, cache
        ) + fib_recursive_cached_generator(n - 1, cache)
    yield cache[n]


@lru_cache
def fib_recursive_lru_cache(n: int) -> int:
    """Fibonacci number using recursion"""
    if n < 2:
        return n
    return fib_recursive(n - 2) + fib_recursive(n - 1)


def fib_recursive_hack(n: int, cache: dict = {}) -> int:
    """Fibonacci number using recursion and caching"""
    if n < 2:
        return n
    if n not in cache:
        cache[n] = fib_recursive_cached(n - 2, cache) + fib_recursive_cached(
            n - 1, cache
        )
    return cache[n]


def main():
    fib_number = 20
    test_iterations = 10000

    print(f"Fibonacci sequence for n = {fib_number}, repeated {test_iterations} times.")

    print(
        "fib_iterative:" + "\t" * 3,
        timeit(
            f"[fib_iterative(i) for i in range({fib_number})]",
            globals=globals(),
            number=test_iterations,
        ),
    )

    print(
        "fib_recursive:" + "\t" * 3,
        timeit(
            f"[fib_recursive(i) for i in range({fib_number})]",
            globals=globals(),
            number=test_iterations,
        ),
    )

    print(
        "fib_recursive_cached:" + "\t" * 2,
        timeit(
            f"[fib_recursive_cached(i, {{}}) for i in range({fib_number})]",
            globals=globals(),
            number=test_iterations,
        ),
    )

    print(
        "fib_recursive_cached_generator:" + "\t",
        timeit(
            f"[fib_recursive_cached_generator(i, {{}}) for i in range({fib_number})]",
            globals=globals(),
            number=test_iterations,
        ),
    )

    print(
        "fib_recursive_lru_cache:" + "\t",
        timeit(
            f"[fib_recursive_lru_cache(i) for i in range({fib_number})]",
            globals=globals(),
            number=test_iterations,
        ),
    )

    print(
        "fib_recursive_hack:" + "\t" * 2,
        timeit(
            f"[fib_recursive_hack(i) for i in range({fib_number})]",
            globals=globals(),
            number=test_iterations,
        ),
    )


if __name__ == "__main__":
    main()
