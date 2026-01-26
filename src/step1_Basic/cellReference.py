import gdspy
import numpy as np

lib = gdspy.GdsLibrary()

ld_fulletch = {"layer": 1, "datatype": 3}
ld_partetch = {"layer": 2, "datatype": 3}
ld_liftoff  = {"layer": 0, "datatype": 7}

p1 = gdspy.Rectangle((-3, -3), (3, 3), **ld_fulletch)
p2 = gdspy.Rectangle((-5, -3), (-3, 3), **ld_partetch)
p3 = gdspy.Rectangle((5, -3), (3, 3), **ld_partetch)
p4 = gdspy.Round((0, 0), 2.5, number_of_points=6, **ld_liftoff)

contact = lib.new_cell("CONTACT")
contact.add([p1, p2, p3, p4]) 

cutout = gdspy.Polygon([
    (0,0),(5,0),(5,5),(0,5),(0,0),
    (2,2),(2,3),(3,3),(3,2),(2,2)
])

device = lib.new_cell("DEVICE")
device.add(cutout)

# Add references
ref1 = gdspy.CellReference(contact, (3.5, 1), magnification=0.25)
ref2 = gdspy.CellReference(contact, (1, 3.5), magnification=0.25, rotation=90)
device.add([ref1, ref2])

top = lib.new_cell("TOP")

#En vez de array, añade una sola referencia:
top.add(gdspy.CellArray(device, 10, 5, (6, 7)))

try:
    lib.write_gds("gds/cellReference.gds")

    gdspy.LayoutViewer()
    print("cellReference.gds generated successfully.")
except Exception as e:
    print("Error generating cellReference.gds:", e)


#lib.write_gds("gds/cellReference.gds")