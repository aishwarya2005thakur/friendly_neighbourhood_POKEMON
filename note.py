def count_dominant_cells(grid):
    if not grid or not grid[0]:
        return 0
    
    n = len(grid)      # Number of rows
    m = len(grid[0])   # Number of columns
    count = 0
    
    # Directions for the 8 neighbors (row_offset, col_offset)
    directions = [
        (-1, -1), (-1, 0), (-1, 1),  # Top-left, Top, Top-right
        (0, -1),          (0, 1),     # Left,        Right
        (1, -1), (1, 0), (1, 1)       # Bottom-left, Bottom, Bottom-right
    ]
    
    # Check each cell in the grid
    for i in range(n):
        for j in range(m):
            is_dominant = True
            current_value = grid[i][j]
            
            # Check all 8 neighbors
            for dx, dy in directions:
                x, y = i + dx, j + dy
                
                # Ensure the neighbor is within bounds
                if 0 <= x < n and 0 <= y < m:
                    if grid[x][y] >= current_value:
                        is_dominant = False
                        break
            
            # If the cell is dominant, increment the count
            if is_dominant:
                count += 1
    
    return count

# Example usage
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result = count_dominant_cells(grid)
print("Number of dominant cells:", result)
