import gdspy
import numpy as np

# ==========================================================
# BASIC SHAPES EXAMPLE  (single cell)
# ==========================================================

# Create a new GDS library
lib = gdspy.GdsLibrary()

#definition of layers:
ld_fulletch = {"layer": 1, "datatype": 3}
ld_partetch = {"layer": 2, "datatype": 3}
ld_liftoff = {"layer": 0, "datatype": 7}

#definition of the rectangles:
p1 = gdspy.Rectangle((-3, -3), (3, 3), **ld_fulletch)
p2 = gdspy.Rectangle((-5, -3), (-3, 3), **ld_partetch)
p3 = gdspy.Rectangle((5, -3), (3, 3), **ld_partetch)
p4 = gdspy.Round((0, 0), 2.5, number_of_points=6, **ld_liftoff)

# Create a cell with a component that is used repeatedly
contact = lib.new_cell("CONTACT")
contact.add([
    gdspy.copy(p1),
    gdspy.copy(p2),
    gdspy.copy(p3),
    gdspy.copy(p4)
])

# Definition of a polygon:
cutout = gdspy.Polygon(
    [(0, 0), (5, 0), (5, 5), (0, 5), (0, 0), (2, 2), (2, 3), (3, 3), (3, 2), (2, 2)]
)

# Create a cell with the complete device
device = lib.new_cell("DEVICE")
device.add(cutout)
# Add 2 references to the component changing size and orientation
ref1 = gdspy.CellReference(contact, (3.5, 1), magnification=0.25)
ref2 = gdspy.CellReference(contact, (1, 3.5), magnification=0.25, rotation=90)
device.add([ref1, ref2])

# The final layout has several repetitions of the complete device
# Top cell for this example
top = lib.new_cell("TOP")
#main = gdspy.Cell("MAIN")
top.add(gdspy.CellArray(device, 3, 2, (6, 7)))


# Write GDS file
try:
    #lib.write_gds("gds/cellReference.gds", cells=[top])
    lib.write_gds("C:/KLayoutTests/cellReference.gds", cells=[top])

    gdspy.LayoutViewer()
    print("cellReference.gds generated successfully.")
except Exception as e:
    print("Error generating cellReference.gds:", e)
