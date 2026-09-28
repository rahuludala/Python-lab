def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return

    tower_of_hanoi(n - 1, source, destination, auxiliary)

    print("Move disk", n, "from", source, "to", destination)

    tower_of_hanoi(n - 1, auxiliary, source, destination)


# For 3 disks
print("Tower of Hanoi for 3 disks:")
tower_of_hanoi(3, "A", "B", "C")

print("\nTotal moves for 3 disks:", 2**3 - 1)


# For 4 disks
print("\nTower of Hanoi for 4 disks:")
tower_of_hanoi(4, "A", "B", "C")

print("\nTotal moves for 4 disks:", 2**4 - 1)
