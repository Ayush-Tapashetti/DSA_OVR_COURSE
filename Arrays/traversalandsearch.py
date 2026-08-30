def section(title):
    print("\n" + "-" * 67)
    print(title)
    print("-" * 67)

def traversal():
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


def linear_search2():
    section("1b. Linear Search + print_array")

    arr = [5, 8, 12, 3, 9]
    print("Array: ", end="")
    print_array(arr)
    print("linear_search(arr, 12) ->", linear_search(arr, 12))
    print("linear_search(arr, 99) ->", linear_search(arr, 99))



if __name__ == "__main__":
    traversal()
    linear_search2()
  