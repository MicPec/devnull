from random import shuffle
from timeit import timeit

# a = [12, 41, 1, 33, 5, 8, 4, 9, 11, 16, 3, 17, 72, 14, 2, 5]
a = list(range(1000))
shuffle(a)


def swap_sort(l: list) -> list:
    for j in range(len(l)):
        for i in range(len(l) - j - 1):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
    return l


def radix_sort(l: list) -> list:

    maxl = len(str(max(l)))

    for i in range(maxl):
        buckets = [[] for _ in range(10)]
        for j in l:
            buckets[j // 10**i % 10].append(j)
        l = []
        for bucket in buckets:
            l.extend(bucket)
    return l


# print(swap_sort(a))
# print(timeit("swap_sort(a)", globals=globals(), number=100))
print(timeit("radix_sort(a)", globals=globals(), number=100))
