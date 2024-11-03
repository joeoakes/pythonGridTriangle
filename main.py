import math


# Function to map Lidar data to a 10x10 grid
def map_lidar_to_grid(lidar_data, grid_size):
    # Create an empty grid
    grid = [[" " for _ in range(grid_size)] for _ in range(grid_size)]

    # Assume the center of the grid is the origin (5, 5) in a 10x10 grid
    center_x, center_y = grid_size // 2, grid_size // 2

    for angle, distance, intensity in lidar_data:
        # Convert angle to radians for calculations
        angle_rad = math.radians(angle)

        # Calculate grid coordinates based on the distance and angle
        x_offset = int(round(center_x + (distance / 10) * math.cos(angle_rad)))  # Scale distance for grid size
        y_offset = int(round(center_y + (distance / 10) * math.sin(angle_rad)))

        # Ensure coordinates are within the grid boundaries
        if 0 <= x_offset < grid_size and 0 <= y_offset < grid_size:
            grid[y_offset][x_offset] = "O"  # Use 'O' to represent an object

    return grid


# Function to display the grid
def display_grid(grid):
    for row in grid:
        print(" | ".join(row))
        print("-" * (len(grid) * 4 - 1))  # Adjust separator length dynamically based on grid size


# Sample Lidar data stream: (angle, distance, intensity)
lidar_data = [
    (12, 9.890625, 211.25),
    (15, 23.640625, 502.25),
    (15, 27.828125, 978.25),
    (10, 29.328125, 993.25)
]

# Create and display the grid with Lidar data
grid_size = 10
lidar_grid = map_lidar_to_grid(lidar_data, grid_size)
display_grid(lidar_grid)
