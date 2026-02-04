# TO RUN: (must be run from ES_CAD2 folder)
# python -m src.step3_Generator.main

import gdspy
from .create_mim_capacitor import create_mim_capacitor

name_file = "mim_option_A_B_offset"
gds_filename = f"gds/{name_file}.gds"

# Create GDS library
lib = gdspy.GdsLibrary()

# Create TOP cell
top = lib.new_cell("TOP_MIM")

# Create a test MIM capacitor option A
mim_cell_A = create_mim_capacitor(
    width=5,      # um (20)
    height=5,     # um (10)
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
    lib.write_gds(gds_filename)
    print(f"{gds_filename} generated successfully.")
except Exception as e:
    print(f"Error generating {gds_filename}: {e}")