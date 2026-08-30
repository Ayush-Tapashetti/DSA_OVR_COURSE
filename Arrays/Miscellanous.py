def section(title):
    print("\n" + "-" * 67)
    print(title)
    print("-" * 67)

# To detect duplicate numbers in an array
def duplicate_check():
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

#Form a number using the digits entered
def form_number_from_digits():
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

#Insert a number in a sorted array
def insert_into_sorted_array():
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

#Higest marks per subject(2D array)
def second_highest_marks():
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

if __name__ == "__main__":
    duplicate_check()
    form_number_from_digits()
    insert_into_sorted_array()
    second_highest_marks()
