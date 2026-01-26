import gdspy
from .create_mim_capacitor import create_mim_capacitor

# Create GDS library
lib = gdspy.GdsLibrary()

# Create a test MIM capacitor
mim_cell = create_mim_capacitor(
    width=20,      # um
    height=10,     # um
    option="A",
    center=(0, 0)
)

# Add cell to library
lib.add(mim_cell)

# Write GDS file
lib.write_gds("test_mim_option_A.gds")

print("GDS file 'test_mim_option_A.gds' generated successfully.")

