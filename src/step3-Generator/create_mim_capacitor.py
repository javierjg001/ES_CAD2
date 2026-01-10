def create_mim_capacitor(
    width, #um^2
    height, #um^2
    option="A", #A or B
    center=(0, 0)):

    import gdspy
    from functions import create_rectangle, create_circle, create_polygon

    LAYERS = {
    "FuseTop":  {"layer": XX, "datatype": YY},
    "Metal2":   {"layer": AA, "datatype": BB},
    "Via2":     {"layer": CC, "datatype": DD},
    "CAP_MK":   {"layer": EE, "datatype": FF},
    "MIM_L_MK": {"layer": GG, "datatype": HH}}


    # Extract coordinates from the "center" parameter (tuple/list (x,y) or dict {"x":..., "y":...})
    if isinstance(center, (tuple, list)) and len(center) == 2:
        center_x, center_y = center
    elif isinstance(center, dict) and 'x' in center and 'y' in center:
        center_x = center['x']
        center_y = center['y']
    else:
        raise TypeError("'center' must be a tuple/list (x, y) or dict with 'x' and 'y' keys")

    # Minimum dimensions check, rule MIM.8a
    if width < 5 or height < 5:
        raise ValueError("MIM area too small (min 5x5 um^2, rule MIM.8a)")

    # Maximum dimensions check, rule MIM.8b
    if width > 100 or height > 100:
        raise ValueError("MIM area too large (max 100x100 um^2, rule MIM.8b)")
    
    # Definition of FuseTop layer
    fuseTop = create_rectangle(
        x = center_x - width/2,
        y = center_y - height/2,
        width = width,
        height = height,
        layer = FUSE_TOP_LAYER)

    # Minimum MiM bottom plate overlap of Top plate (0.6um) (rule MIM.3)
    metal2 = offset_shape(fuseTop, distance=0.6, layer=METAL2_LAYER)


