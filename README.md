# Advent of Code 2020
## Performance of Python solutions
Calculated using the `timeit` library. File loading might or might not be included in the time. Output of `benchmark.py`:

```
BENCHMARK DAY 01:
Ran part1() 100 times, average result: 0.00099 seconds
Ran part2() 100 times, average result: 0.00062 seconds

BENCHMARK DAY 02:
Ran part1() 100 times, average result: 0.00452 seconds
Ran part2() 100 times, average result: 0.00250 seconds

BENCHMARK DAY 03:
Ran part1() 100 times, average result: 0.00023 seconds
Ran part2() 100 times, average result: 0.00048 seconds

BENCHMARK DAY 04:
Ran parse_and_count_valid() 100 times, average result: 0.00413 seconds

BENCHMARK DAY 05:
Part 1: Ran max_seat_id() 100 times, average result: 0.00207 seconds
Part 2: Ran find_seat() 100 times, average result: 0.00216 seconds

BENCHMARK DAY 06:
Ran solve() 100 times, average result: 0.00623 seconds

BENCHMARK DAY 07 (Before memoization):
Ran part1() 100 times, average result: 0.03604 seconds
Ran part2() 100 times, average result: 0.00275 seconds

BENCHMARK DAY 07 (After memoization):
Ran part1() 100 times, average result: 0.00306 seconds
Ran part2() 100 times, average result: 0.00246 seconds
> 10x improvement for part 1!

BENCHMARK DAY 08:
Ran part1() 100 times, average result: 0.00069 seconds
Ran part2() 100 times, average result: 0.05584 seconds

BENCHMARK DAY 09:
PART 1: Ran find_weird_num() 100 times, average result: 0.00788 seconds
PART 2: Ran find_weird_sum() 100 times, average result: 0.31751 seconds

BENCHMARK DAY 10:
PART 1: Ran greedy_longest_path() 100 times, average result: 0.00021 seconds
PART 2: Ran find_num_paths() 100 times, average result: 0.00035 seconds

BENCHMARK DAY 11:
PART 1: Ran solve() 100 times, average result: 1.74533 seconds
PART 2: Ran solve() 100 times, average result: 6.67888 seconds 😳

BENCHMARK DAY 12:
PART 1: Ran distance_travelled_p1() 100 times, average result: 0.00079 seconds
PART 2: Ran distance_travelled_p2() 100 times, average result: 0.00073 seconds
```