def section(title):
    print("\n" + "-" * 67)
    print(title)
    print("-" * 67)

def merge():
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


if __name__ == "__main__":
    merge()
