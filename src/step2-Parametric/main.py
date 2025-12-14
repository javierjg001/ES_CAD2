import gdspy
import numpy as np
from functions import *

# ==========================================================
# MAIN PARAMETRIC SHAPES
# ==========================================================

# Create a new GDS library
lib = gdspy.GdsLibrary()

# Top cell for this example
top = lib.new_cell("TOP_PARAMETRIC")

# add rectangle using the function
top.add(create_rectangle(0, 0, 10, 20, layer=0, datatype=0))
top.add(create_circle(10, 10, 5, layer=10, datatype=0))
top.add(create_polygon([(20, 0), (25, 10), (30, 0), (35,10)], layer=50, datatype=0))

top.add(offset_shape(create_rectangle(40, -30, 10, 20), distance=10, layer=10, datatype=0))
top.add(rotate_shape(create_rectangle(40, 0, 10, 10, layer=20, datatype=0), angle=np.pi/4))
top.add(scale_shape(create_polygon([(20, -20), (25, -10), (30, -20), (35,-10)], layer=60, datatype=0), scalex=3, scaley=0.5))
top.add(translate_shape(create_rectangle(50, 0, 10, 10, layer=30, datatype=0), dx=5, dy=5))


# Write GDS file
try:
    lib.write_gds("gds/parametric_shapes.gds")
    print("parametric_shapes.gds generated successfully.")
except Exception as e:
    print("Error generating parametric_shapes.gds:", e)