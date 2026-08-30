def section(title):
    print("\n" + "-" * 67)
    print(title)
    print("-" * 67)

def two_sum_naive(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return True
    return False


def two_sum_two_pointer(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        total = arr[left] + arr[right]
        if total == target:
            return True
        elif total < target:
            left += 1     # need a bigger sum -> move left pointer right
        else:
            right -= 1    # need a smaller sum -> move right pointer left
    return False


def two_pointer():
    section("5. Two-Pointer Technique — Pair Summing to a Target")

    arr = [0, -1, 2, -3, 1]
    target = -2
    print("Naive two_sum:", two_sum_naive(arr, target))

    arr_sorted = [-3, -1, 0, 1, 2]   # already sorted
    print("Two-pointer two_sum (sorted input):", two_sum_two_pointer(arr_sorted, target))

if __name__ == "__main__":
    two_pointer()

