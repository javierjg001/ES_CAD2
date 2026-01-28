import gdspy
from .create_mim_capacitor import create_mim_capacitor

# Create GDS library
lib = gdspy.GdsLibrary()

# Create TOP cell
top = lib.new_cell("TOP_MIM")

# Create a test MIM capacitor option A
mim_cell_A = create_mim_capacitor(
    width=20,      # um
    height=10,     # um
    option="A",
    center=(0, 0)
)

# Create a test MIM capacitor option B
mim_cell_B = create_mim_capacitor(
    width=30,      # um
    height=15,     # um
    option="B",
    center=(0, 0)
)

# Add MIM cells to library
lib.add(mim_cell_A)
lib.add(mim_cell_B)

# Instantiate them in TOP
top.add(gdspy.CellReference(mim_cell_A, (0, 0)))
top.add(gdspy.CellReference(mim_cell_B, (60, 0))) 

lib.add(top)

# Write GDS file
try:
    lib.write_gds("gds/mim_option_A_B.gds")
    print("mim_option_A_B.gds generated successfully.")
except Exception as e:
    print("Error generating mim_option_A_B.gds:", e)

