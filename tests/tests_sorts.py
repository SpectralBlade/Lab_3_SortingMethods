import pytest
from typing import Callable
from Lab_3_SortingMethods.tests.gen_test_sorts import (
    rand_int_array,
    nearly_sorted,
    many_duplicates,
    rand_float_array,
)

from Lab_3_SortingMethods.src.sort_methods.bubble_sort import bubble_sort
from Lab_3_SortingMethods.src.sort_methods.quick_sort import quick_sort
from Lab_3_SortingMethods.src.sort_methods.heap_sort import heap_sort
from Lab_3_SortingMethods.src.sort_methods.counting_sort import counting_sort
from Lab_3_SortingMethods.src.sort_methods.radix_sort import radix_sort
from Lab_3_SortingMethods.src.sort_methods.bucket_sort import bucket_sort

from Lab_3_SortingMethods.tests.gen_test_sorts import generate_test_with_key_cmp
from functools import cmp_to_key

@pytest.fixture(params=[bubble_sort, quick_sort, heap_sort, sorted])
def sorting_algorithm(request):
    return request.param

@pytest.fixture(params=[counting_sort, radix_sort, sorted])
def integer_sorting_algorithm(request):
    return request.param

@pytest.fixture(params=[bucket_sort, sorted])
def float_sorting_algorithm(request):
    return request.param

class TestSortingAlgorithms:

    BASIC_CASES = [
        [],
        [1],
        [1, 2],
        [2, 1],
        [1, 2, 3],
        [3, 2, 1],
        [1, 3, 2],
        [1, 1, 1],
        [1, 2, 1],
    ]

    @pytest.mark.parametrize("test_case", BASIC_CASES)
    def test_basic_cases(self, sorting_algorithm: Callable, test_case: list[int]):
        result = sorting_algorithm(test_case.copy())
        assert result == sorted(test_case)

    def test_random_arrays(self, sorting_algorithm):
        test_cases = [
            rand_int_array(10, 1, 100, seed=3456008672),
            rand_int_array(50, -100, 100, seed=89765899678),
            rand_int_array(100, 1, 1000, seed=78968853424),
        ]
        for arr in test_cases:
            result = sorting_algorithm(arr.copy())
            assert result == sorted(arr)

    def test_nearly_sorted_arrays(self, sorting_algorithm: Callable):
        test_cases = [
            nearly_sorted(20, 2, seed=96785476862),
            nearly_sorted(30, 5, seed=567849988073),
            nearly_sorted(50, 10, seed=123345888657),
        ]
        for arr in test_cases:
            result = sorting_algorithm(arr.copy())
            assert result == sorted(arr)

    def test_arrays_with_duplicates(self, sorting_algorithm: Callable):
        test_cases = [
            many_duplicates(20, 3, seed=876879868762),
            many_duplicates(30, 5, seed=489989778903),
        ]
        for arr in test_cases:
            result = sorting_algorithm(arr.copy())
            assert result == sorted(arr)

class TestBucketSort:
    def test_bucket_sort_basic(self, float_sorting_algorithm: Callable):
        test_cases = [
            [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51],
            [0.1, 0.5, 0.9, 0.2, 0.8, 0.3, 0.7, 0.4, 0.6],
        ]
        for arr in test_cases:
            result = float_sorting_algorithm(arr.copy())
            assert result == sorted(arr)

    def test_bucket_sort_out_of_range(self):
        with pytest.raises(ValueError):
            bucket_sort([1.5, 0.5, 0.3])
        with pytest.raises(ValueError):
            bucket_sort([-0.1, 0.5, 0.3])

    def test_float_arrays(self, float_sorting_algorithm: Callable):
        test_cases = [
            rand_float_array(20, 0.0, 1.0, seed=42),
            rand_float_array(30, 0.0, 1.0, seed=43),
        ]
        for arr in test_cases:
            arr = [abs(x) % 1.0 for x in arr]
            result = float_sorting_algorithm(arr.copy())
            expected = sorted(arr)
            for r, e in zip(result, expected):
                assert abs(r - e) < 1e-10

class TestValueErrorsInSorts:
    def test_value_errors(self, sorting_algorithm: Callable):
        with pytest.raises(ValueError):
            counting_sort([-5, -2, -20, 4, 1.3])
            counting_sort([1.2, 3.1, 4.3, 2.2])
        with pytest.raises(ValueError):
            radix_sort([-5, -2, -20, 4])
            radix_sort([1.2, 3.1, 4.3, 2.2])

class TestSortingWithKeyAndCmp:
    @pytest.mark.parametrize("sorting_algorithm", [bubble_sort, quick_sort, heap_sort])
    def test_sort_with_random_keys(self, sorting_algorithm: Callable):
        for _ in range(10):
            arr, key, cmp_fn = generate_test_with_key_cmp(
                n=20, lo=-50, hi=50, want_key=True, want_cmp=False
            )

            result = sorting_algorithm(arr.copy(), key=key)
            expected = sorted(arr, key=key)

            assert result == expected

    @pytest.mark.parametrize("sorting_algorithm", [bubble_sort, quick_sort, heap_sort])
    def test_sort_with_random_cmp(self, sorting_algorithm: Callable):
        for _ in range(10):
            arr, key, cmp_fn = generate_test_with_key_cmp(
                n=20, lo=-50, hi=50, want_key=False, want_cmp=True
            )

            result = sorting_algorithm(arr.copy(), cmp=cmp_fn)
            expected = sorted(arr, key=cmp_to_key(cmp_fn))

            assert result == expected