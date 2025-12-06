from typing import Callable, Any
import random, numpy

def rand_int_array(n: int, lo: int, hi: int, *, distinct: bool = False, seed = None) -> list[int]:
    if seed is not None:
        random.seed(seed)

    if distinct:
        if n > (hi - lo + 1):
            raise ValueError(f"Невозможно сгенерировать {n} уникальных чисел в диапазоне [{lo}, {hi}]")

        population = list(range(lo, hi + 1))
        return random.sample(population, n)
    else:
        return [random.randint(lo, hi) for _ in range(n)]

def nearly_sorted(n: int, swaps: int, *, seed=None) -> list[int]:
    if seed is not None:
        random.seed(seed)

    array = list(range(n))
    for _ in range(swaps):
        i, j = random.sample(range(n), 2)
        array[i], array[j] = array[j], array[i]

    return array

def many_duplicates(n: int, k_unique=5, *, seed=None) -> list[int]:
    if seed is not None:
        random.seed(seed)

    if k_unique <= 0:
        raise ValueError("k_unique должен быть положительным")

    unique_values = random.sample(range(-n, 2 * n), k_unique)
    return [random.choice(unique_values) for _ in range(n)]

def rand_float_array(n: int, lo=0.0, hi=1.0, *, seed=None) -> list[float]:
    if seed is not None:
        random.seed(seed)
        numpy.random.seed(seed)

    return [random.uniform(lo, hi) for _ in range(n)]

def random_key_function() -> Callable[[Any], Any]:
    options = []

    options.append(lambda x: x)
    options.append(lambda x: -x)
    options.append(lambda x: abs(x))
    options.append(lambda x: str(x))
    options.append(lambda x: len(str(x)))

    return random.choice(options)

def random_comparator() -> Callable[[Any, Any], int]:

    def cmp_basic(a, b):
        return (a > b) - (a < b)
    def cmp_reverse(a, b):
        return (b > a) - (b < a)
    def cmp_abs(a, b):
        return (abs(a) > abs(b)) - (abs(a) < abs(b))
    def cmp_str(a, b):
        return (str(a) > str(b)) - (str(a) < str(b))
    def cmp_strlen(a, b):
        return (len(str(a)) > len(str(b))) - (len(str(a)) < len(str(b)))

    return random.choice([cmp_basic, cmp_reverse, cmp_abs, cmp_str, cmp_strlen])


def generate_test_with_key_cmp(
        n: int,
        *,
        lo: int = -100,
        hi: int = 100,
        seed: int | None = None,
        want_key: bool = True,
        want_cmp: bool = False
    ) -> tuple[list[Any], Callable | None, Callable | None]:

    if seed is not None:
        random.seed(seed)

    arr = rand_int_array(n, lo, hi)

    key = random_key_function() if want_key else None
    cmp_fn = random_comparator() if want_cmp else None

    if want_cmp:
        key = None

    return arr, key, cmp_fn