

def move_disk(src_stack, dest_stack, src_name, dest_name):
    disk = src_stack.pop()
    dest_stack.append(disk)
    print(f"Moved Disk {disk}: {src_name} ➔ {dest_name}")


def tower_of_hanoi(n, src, aux, dest, src_name, aux_name, dest_name):
    if n == 1:
        move_disk(src, dest, src_name, dest_name)
        return

    tower_of_hanoi(n - 1, src, dest, aux, src_name, dest_name, aux_name)
    move_disk(src, dest, src_name, dest_name)
    tower_of_hanoi(n - 1, aux, src, dest, aux_name, src_name, dest_name)


if __name__ == "__main__":

    rodA = [3, 2, 1] 
    rodB = []
    rodC = []

    print(f"Starting State:")
    print(f"ROD A: {rodA}\nROD B: {rodB}\nROD C: {rodC}\n")

    tower_of_hanoi(len(rodA), rodA, rodB, rodC, "ROD A", "ROD B", "ROD C")

    print(f"Final State:")
    print(f"ROD A: {rodA}\nROD B: {rodB}\nROD C: {rodC}")