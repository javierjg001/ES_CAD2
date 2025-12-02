import gdspy

# Crear biblioteca GDS
lib = gdspy.GdsLibrary()

# Crear una celda
cell = lib.new_cell('TEST')

# Crear un rectángulo simple de prueba
rect = gdspy.Rectangle((0, 0), (10, 5), layer=1)
cell.add(rect)

# Guardar el archivo GDS
lib.write_gds('gds/primer_test.gds')

print("GDS generado correctamente.")
