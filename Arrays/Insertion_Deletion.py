def section(title):
    print("\n" + "-" * 67)
    print(title)
    print("-" * 67)

#Insertion
def insertion():
    section("2. Inserting an Element")

    arr = [10, 20, 30, 40, 50]
    item = 99
    pos = 2   # inserting at index 2

    # increase size
    arr.append(None)

    print("Before Insertions", arr)

    # shift elements right
    for i in range(len(arr) - 2, pos - 1, -1):
        arr[i + 1] = arr[i]

    # place new element
    arr[pos] = item
    print("Array after insertion:", arr)

#Deletion
def deletion():
    section("3. Array Deletion")

    arr = [10, 20, 30, 40, 50]
    pos = 2   # delete the element at index 2 (value = 30)

    print("Before deletion", arr)

    # shift elements left
    for i in range(pos, len(arr) - 1):
        arr[i] = arr[i + 1]
    arr.pop()

    print("Array after deletion:", arr)

if __name__ == "__main__":
    insertion()
    deletion()
