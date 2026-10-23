import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from pathlib import Path

# This script generates an occupancy grid based on the input vectors provided in a text file. The occupancy grid is represented as a matrix, where different values correspond to different types of areas (e.g., floor, wall, door, area to avoid). The script reads the input vectors, processes them to create the occupancy grid, and then displays the grid as an image.

# USER-DEFINED VARIABLES
input_vector_file = "test_vectors.txt" # change to measurements.txt to see current workings of Broun Hall occupancy grid
c = 4 # constant factor that each dimension will be multiplied by; the amount of virtual space allocated to 1 inch of real space

def create_matrix(line):
    # Split the first line into individual numbers to get matrix dimensions
    line = line.replace('(', '').replace(')', '').replace('[', '').replace(']', '')
    numbers = list(map(float, line.split(',')))

    # Create a matrix of zeros with dimensions based on the input numbers and the constant factor c
    n = (int(numbers[0] * c))
    m = (int(numbers[1] * c))
    
    # Fill the matrix with zeros
    matrix = [[0 for _ in range(m)] for _ in range(n)]

    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(''.join(map(str, row)))
        
def separate_hor_vert(list):
    horizontal = []
    vertical = []
    for i in range(0, len(list), 2):
        item = list[i]
        pair = list[i + 1]
        if item.startswith('-h'):
            horizontal.append(item[4:-1].replace(" ", ""))
            horizontal.append(pair)
        elif item.startswith('-v'):
            vertical.append(item[4:-1].replace(" ", ""))
            vertical.append(pair)

    return horizontal, vertical

def process_horizontal(line1, line2, matrix):
    line1 = line1.replace("(", "").replace(")", "")
    x1, y1, x2, y2 = [
        round(float(value) * c)
        for value in line1.split(',')
    ]
    y = len(matrix) - y1 - 1
    print(line2)
    data = line2.split(",")
    for i in range(0, len(data), 2): # for each tuple 
        type = int(data[i])
        length = round(float(data[i + 1]) * c)
        for x in range(x1, min(x1 + length, len(matrix[0]))):
            for t in range(c):
                y_pos = y - t
                if 0 <= y_pos < len(matrix):
                    matrix[y_pos][x] = type
        x1 += length
        
def process_vertical(line1, line2, matrix):
    line1 = line1.replace("(", "").replace(")", "")
    x1, y1, x2, y2 = [
        round(float(value) * c)
        for value in line1.split(',')
    ]
    x = x1
    print(line2)
    data = line2.split(",")
    for i in range(0, len(data), 2): # for each tuple 
        type = int(data[i])
        length = round(float(data[i + 1]) * c)
        for y in range(y1, min(y1 + length, len(matrix))):
           for y in range(y1, min(y1 + length, len(matrix))):
                for t in range(c):
                    x_pos = x + t
                    if 0 <= x_pos < len(matrix[0]):
                        matrix[len(matrix) - y - 1][x_pos] = type
        y1 += length
        
def display_as_image(matrix):
    plt.imshow(matrix, cmap="pink", interpolation="nearest")
    legend_items = [
        Patch(facecolor=plt.cm.pink(0.0), label="Floor"),
        Patch(facecolor=plt.cm.pink(0.25), label="Wall"),
        Patch(facecolor=plt.cm.pink(0.75), label="Door"),
        Patch(facecolor=plt.cm.pink(1.0), label="Area to Avoid")
    ]

    plt.legend(handles=legend_items, loc="upper right", bbox_to_anchor=(1.35, 1))
    plt.show()
    
# Get the parent directory of the current script
parent_dir = Path(__file__).resolve().parent.parent

# Construct the path to the file inside the subdirectory
file_path = parent_dir / 'tests' / input_vector_file # change to measurements.txt to see current workings of Broun Hall occupancy grid

# Open and read the file    
with open(file_path, "r") as file:
    lines = [line.strip() for line in file]

# Create an empty matrix
matrix = create_matrix(lines[0])

# Separate walls parallel to x-axis from those parallel to y-axis
(horizontal, vertical) = separate_hor_vert(lines[1:])

# Generate a row in the matrix for each wall parallel to the x-axis
for i in range(0, len(horizontal), 2):
    process_horizontal(horizontal[i], horizontal[i + 1], matrix)
    
# Generate a column in the matrix for each wall parallel to the y-axis
for i in range(0, len(vertical), 2):
    process_vertical(vertical[i], vertical[i + 1], matrix)
    
# Print as an image
print("Map:")
display_as_image(matrix)
