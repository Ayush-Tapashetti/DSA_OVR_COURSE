"""
MASTER CODE — Arrays
====================
Every code example from Arrays_Guide.md, expanded into a fully self-contained,
runnable version — each with sample data and printed output so you can run
this file directly and see every concept work.

Run:  python master_arrays.py
"""

def section(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


# =====================================================================
# 1. TRAVERSAL
# =====================================================================
def demo_traversal():
    section("1. Traversal")

    arr = [10, 20, 30, 40]
    for i in range(len(arr)):
        print("index", i, "value", arr[i])


def linear_search(arr, target):
    i = 0
    while i < len(arr):
        if arr[i] == target:
            return i        # target found
        i += 1
    return -1                # target not found


def print_array(arr):
    i = 0
    while i < len(arr):
        print(arr[i], end=" ")
        i += 1
    print()


def demo_linear_search():
    section("1b. Linear Search + print_array")

    arr = [5, 8, 12, 3, 9]
    print("Array: ", end="")
    print_array(arr)
    print("linear_search(arr, 12) ->", linear_search(arr, 12))
    print("linear_search(arr, 99) ->", linear_search(arr, 99))


# =====================================================================
# 2. INSERTION
# =====================================================================
def demo_insertion():
    section("2. Inserting an Element")

    arr = [10, 20, 30, 40, 50]
    item = 99
    pos = 2   # inserting at index 2

    # increase size
    arr.append(None)

    # shift elements right
    for i in range(len(arr) - 2, pos - 1, -1):
        arr[i + 1] = arr[i]

    # place new element
    arr[pos] = item
    print("Array after insertion:", arr)


# =====================================================================
# 3. DELETION
# =====================================================================
def demo_deletion():
    section("3. Array Deletion")

    arr = [10, 20, 30, 40, 50]
    pos = 2   # delete the element at index 2 (value = 30)

    # shift elements left
    for i in range(pos, len(arr) - 1):
        arr[i] = arr[i + 1]
    arr.pop()

    print("Array after deletion:", arr)


# =====================================================================
# 4. MERGING TWO ARRAYS
# =====================================================================
def demo_merge():
    section("4. Merging Two Arrays")

    A = [10, 20, 30]
    B = [40, 50, 60]
    C = []           # merged array

    # copy elements of A
    for i in range(len(A)):
        C.append(A[i])
    # copy elements of B
    for j in range(len(B)):
        C.append(B[j])

    print("Merged Array:", C)


# =====================================================================
# 5. TWO-POINTER TECHNIQUE
# =====================================================================
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


def demo_two_pointer():
    section("5. Two-Pointer Technique — Pair Summing to a Target")

    arr = [0, -1, 2, -3, 1]
    target = -2
    print("Naive two_sum:", two_sum_naive(arr, target))

    arr_sorted = [-3, -1, 0, 1, 2]   # already sorted
    print("Two-pointer two_sum (sorted input):", two_sum_two_pointer(arr_sorted, target))


# =====================================================================
# 6. SOLVED PRACTICE PROBLEMS
# =====================================================================
def demo_duplicate_check():
    section("6.1 Detect a duplicate number in an array")

    arr = [10, 20, 30, 40, 20]
    duplicate_found = False
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                duplicate_found = True
                break
        if duplicate_found:
            break

    if duplicate_found:
        print("Duplicate element found")
    else:
        print("No duplicate elements")


def demo_form_number_from_digits():
    section("6.2 Form a number from n digits (non-interactive demo)")

    # Original version reads input(); here we simulate the same logic
    # with a fixed list of digits so the script runs unattended.
    digits = [3, 7, 9]   # pretend the user entered these one at a time
    arr = []
    for d in digits:
        arr.append(d)

    number = 0
    for i in range(len(arr)):
        number = number * 10 + arr[i]

    print("Digits entered:", digits)
    print("Formed Number:", number)


def demo_insert_into_sorted_array():
    section("6.3 Insert a number into an already-sorted array")

    arr = [10, 20, 30, 40, 60]
    item = 50
    pos = 0
    while pos < len(arr) and arr[pos] < item:
        pos += 1
    arr.append(None)
    for i in range(len(arr) - 2, pos - 1, -1):
        arr[i + 1] = arr[i]
    arr[pos] = item
    print("Array after insertion:", arr)


def demo_2d_highest_marks():
    section("6.4 2D Array — highest marks per subject (non-interactive demo)")

    # Original version reads input() for 5 students x 3 subjects;
    # here we simulate the same logic with fixed sample marks.
    marks = [
        [78, 65, 90],
        [88, 72, 95],
        [60, 55, 80],
        [92, 81, 70],
        [74, 90, 85],
    ]
    print("Marks matrix (rows = students, columns = subjects):")
    for row in marks:
        print(row)

    highest = [0, 0, 0]   # for 3 subjects
    for j in range(3):
        for i in range(5):
            if marks[i][j] > highest[j]:
                highest[j] = marks[i][j]

    print("\nHighest marks in each subject:")
    for j in range(3):
        print(f"Subject {j+1}: {highest[j]}")


# =====================================================================
# RUN EVERYTHING
# =====================================================================
if __name__ == "__main__":
    demo_traversal()
    demo_linear_search()
    demo_insertion()
    demo_deletion()
    demo_merge()
    demo_two_pointer()
    demo_duplicate_check()
    demo_form_number_from_digits()
    demo_insert_into_sorted_array()
    demo_2d_highest_marks()
    print("\n" + "=" * 70)
    print("ALL ARRAY DEMOS COMPLETE")
    print("=" * 70)
