from itertools import combinations

def has_all_digits(nums):
    digit_set = set()
    for num in nums:
        digit_set.update(num)
    return len(digit_set) == 10

t = int(input())
for _ in range(t):
    n = int(input())
    arr = input().split()

    for triple in combinations(arr, 3):
        if has_all_digits(triple):
            print(*triple)
            break
