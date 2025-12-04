import gdspy
import numpy as np

# Create GDS library
lib = gdspy.GdsLibrary()

# Create a cell
cell = lib.new_cell('HEART')

# -------------------------
# Generate heart curve points
# -------------------------
t = np.linspace(0, 2 * np.pi, 400)

x = 16 * np.sin(t)**3
y = (13 * np.cos(t) -
     5 * np.cos(2 * t) -
     2 * np.cos(3 * t) -
     np.cos(4 * t))

# Scale and move the heart
scale = 1.0       # change this to modify the size
x = x * scale + 50   # shift to the right
y = y * scale + 50   # shift upward

# Combine points into list of tuples
points = list(zip(x, y))

# Create polygon on layer 1
heart = gdspy.Polygon(points, layer=1)

cell.add(heart)

# Save the GDS file
lib.write_gds('gds/heart_shape.gds')

print("GDS generated successfully.")
