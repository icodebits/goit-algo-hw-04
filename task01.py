import timeit
import random

from merge_sort import merge_sort
from insertion_sort import insertion_sort

# Генерація випадкового масиву для тестування
arr_small = [random.randint(1, 1000) for _ in range(1000)]
arr_big   = [random.randint(1, 10000) for _ in range(10000)]

# Вимірюємо час для merge_sort
merge_sort_time_small = timeit.timeit(lambda: merge_sort(arr_small.copy()), number=10)

# Вимірюємо час для insertion_sort
insertion_sort_time_small = timeit.timeit(lambda: insertion_sort(arr_small.copy()), number=10)

# Вимірюємо час для Timsort
timsort_time_small = timeit.timeit(lambda: sorted(arr_small.copy()), number=10)

# Вимірюємо час для merge_sort
merge_sort_time_big = timeit.timeit(lambda: merge_sort(arr_big.copy()), number=10)

# Вимірюємо час для insertion_sort
insertion_sort_time_big = timeit.timeit(lambda: insertion_sort(arr_big.copy()), number=10)

# Вимірюємо час для Timsort
timsort_time_big = timeit.timeit(lambda: sorted(arr_big.copy()), number=10)

print(f"{'| Algorithm': <20} | {'Time Small': <20} | {'Time Big': <20}")

print(f":{'-'*19} | :{'-'*19} | :{'-'*19}")

print(f"{'| Merge Sort': <20} | {merge_sort_time_small:<20.5f} | {merge_sort_time_big:<20.5f}")
print(f"{'| Insertion Sort': <20} | {insertion_sort_time_small:<20.5f} | {insertion_sort_time_big:<20.5f}")
print(f"{'| Timsort': <20} | {timsort_time_small:<20.5f} | {timsort_time_big:<20.5f}")


