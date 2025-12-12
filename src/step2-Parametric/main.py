import gdspy
import numpy as np
from functions import create_rectangle

# ==========================================================
# MAIN PARAMETRIC SHAPES
# ==========================================================

# Create a new GDS library
lib = gdspy.GdsLibrary()

# Top cell for this example
top = lib.new_cell("TOP_PARAMETRIC")

# add rectangle using the function
top.add(create_rectangle(0, 0, 10, 10, layer=10, datatype=0))

# Write GDS file
try:
    lib.write_gds("gds/parametric_shapes.gds", cells=[top])
    print("parametric_shapes.gds generated successfully.")
except Exception as e:
    print("Error generating parametric_shapes.gds:", e)