import gdspy
import numpy as np

# ==========================================================
# FUNCTIONS PARAMETRIC SHAPES
# ==========================================================

# --------------------RECTANGLE FUNCTION-------------------------
def create_rectangle(x, y, width, height, layer=1, datatype=0):
    return gdspy.Rectangle(
        (x, y),
        (x + width, y + height),
        layer=layer,
        datatype=datatype
    )

# --------------------CIRCLE FUNCTION-------------------------
def create_circle(center_x, center_y, radius, layer=1, datatype=0, num_points=64):
    return gdspy.Round(
        (center_x, center_y),
        radius,
        number_of_points=num_points,
        layer=layer,
        datatype=datatype
    )

# --------------------POLYGON FUNCTION-------------------------
def create_polygon(points, layer=1, datatype=0):
    return gdspy.Polygon(points, layer=layer, datatype=datatype)

# Offset example: outline of the rectangle
def offset_shape(shape, distance, layer=1, datatype=0):
    return gdspy.offset(
        shape,
        distance=distance,
        join_first=True,
        layer=layer,
        datatype=datatype
    )

# ==========================================================
# FUNCTIONS PARAMETRIC TRANSFORMATIONS
# ==========================================================

# --------------------ROTATE FUNCTION-------------------------
def rotate_shape(shape, angle, center=None):
    if center is None:
        bb = shape.get_bounding_box()
        center = (
            (bb[0][0] + bb[1][0]) / 2,
            (bb[0][1] + bb[1][1]) / 2
        )
    shape.rotate(angle, center)
    return shape

