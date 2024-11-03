import math


# Function to simulate trilateration and find the point on the grid
def trilateration(beacon1, beacon2, beacon3):
    # Unpack the beacon data: (x, y, range)
    x1, y1, r1 = beacon1
    x2, y2, r2 = beacon2
    x3, y3, r3 = beacon3

    # Solve the equations for trilateration
    A = 2 * (x2 - x1)
    B = 2 * (y2 - y1)
    D = 2 * (x3 - x1)
    E = 2 * (y3 - y1)

    C = r1 ** 2 - r2 ** 2 - x1 ** 2 - y1 ** 2 + x2 ** 2 + y2 ** 2
    F = r1 ** 2 - r3 ** 2 - x1 ** 2 - y1 ** 2 + x3 ** 2 + y3 ** 2

    # Calculate x and y coordinates
    x = (C * E - F * B) / (A * E - D * B)
    y = (C * D - A * F) / (B * D - A * E)

    return round(x), round(y)


# Function to display a 10x10 grid with the calculated point and beacons
def display_grid_with_beacons(beacons, x, y, grid_size=10):
    grid = [[" " for _ in range(grid_size)] for _ in range(grid_size)]

    # Place the beacons on the grid
    for i, (bx, by, _) in enumerate(beacons, start=1):
        if 0 <= bx < grid_size and 0 <= by < grid_size:
            grid[by][bx] = f"B{i}"  # Label beacons as B1, B2, B3, etc.

    # Place the trilateration point on the grid
    if 0 <= x < grid_size and 0 <= y < grid_size:
        grid[y][x] = "X"  # Mark the calculated point

    # Display the grid
    for row in grid:
        print(" | ".join(row))
        print("-" * (len(grid) * 4 - 1))


# Example beacon data (x, y, range)
beacon1 = (1, 3, 3.5)
beacon2 = (7, 1, 4.0)
beacon3 = (4, 8, 3.0)

beacons = [beacon1, beacon2, beacon3]

# Calculate the trilateration point and display the grid
x, y = trilateration(beacon1, beacon2, beacon3)
print(f"Trilateration point: ({x}, {y})")
display_grid_with_beacons(beacons, x, y)
