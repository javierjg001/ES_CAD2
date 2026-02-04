import gdspy
import numpy as np

# ==========================================================
# BASIC SHAPES EXAMPLE  (single cell)
# ==========================================================

# Create a new GDS library
lib = gdspy.GdsLibrary()

# Top cell for this example
top = lib.new_cell("TOP_BASIC")

# Rectangle
rect = gdspy.Rectangle((0, 0), (10, 10), layer=10)

# Circle
circle = gdspy.Round((25, 5), 7, layer=20, datatype=0)

# Zig-zag polygon
points = [
    (0, 0), (2, 2), (2, 6),
    (-6, 6), (-6, -6),
    (-4, -4), (-4, 4), (0, 4)
]
poly = gdspy.Polygon(points)
# Apply transformations: rotate and scale
poly.rotate(np.pi / 2.0)   # 90 degrees
poly.scale(1, 0.5)

# Text + boolean operation (text cut out of a rectangle)
text = gdspy.Text("GDSPY", 4, (35, 0))
bb = np.array(text.get_bounding_box())
rect_text = gdspy.Rectangle(bb[0] - 1, bb[1] + 1)
inv = gdspy.boolean(rect_text, text, "not", layer=0, datatype=0)

# Offset example: outline of the rectangle
outline = gdspy.offset(rect, distance=2, join_first=True, layer=11, datatype=0)

# Add everything to the top cell
top.add(rect)
top.add(circle)
top.add(poly)
top.add(inv)
top.add(outline)

# Write GDS file
try:
    lib.write_gds("gds/basic_shapes.gds")
    print("basic_shapes.gds generated successfully.")
except Exception as e:
    print("Error generating basic_shapes.gds:", e)
