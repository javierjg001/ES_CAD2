def create_mim_capacitor(
    width, #um^2
    height, #um^2
    option="A", #A or B
    center=(0, 0)):

    import gdspy
    from functions import create_rectangle, create_circle, create_polygon

    LAYERS = {
    "FuseTop":  {"layer": 75, "datatype": 0},
    "Metal2":   {"layer": 36, "datatype": 0},
    "Via2":     {"layer": 38, "datatype": 0},
    "Metal3":   {"layer": 42, "datatype": 0},
    "CAP_MK":   {"layer": 117, "datatype": 5},
    "MIM_L_MK": {"layer": 117, "datatype": 10},
    }

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
        **LAYERS["FuseTop"]) #same thing as putting: layer=LAYERS["FuseTop"]["layer"], datatype=LAYERS["FuseTop"]["datatype"]
    
    # Minimum MiM bottom plate overlap of Top plate (0.6um) (Virtual bottom plate from FuseTop) (rule MIM.3)
    metal2 = offset_shape(fuseTop, distance=0.6, **LAYERS["Metal2"])
    
    # FuseTop enclosure by CAP_MK = 0, rule MIM.7
    cap_mk = create_rectangle(
        x = center_x - width/2,
        y = center_y - height/2,
        width = width,
        height = height,
        **LAYERS["CAP_MK"]
    )

    # MIM_L_MK to identify capacitor length, rule MIM.12
    MIM_L_MK_THICKNESS = 0.2  # um (marker thickness)

    if width >= height:
        # Length along X (width)
        mim_l_mk = create_rectangle(
            x = center_x - width/2,
            y = center_y - MIM_L_MK_THICKNESS/2,
            width = width,
            height = MIM_L_MK_THICKNESS,
            **LAYERS["MIM_L_MK"]
        )
    else:
        # Length along Y (height)
        mim_l_mk = create_rectangle(
            x = center_x - MIM_L_MK_THICKNESS/2,
            y = center_y - height/2,
            width = MIM_L_MK_THICKNESS,
            height = height,
            **LAYERS["MIM_L_MK"]
        )

    # Metal3 top plate (coincident with FuseTop area)
    metal3 = create_rectangle(
        x = center_x - width/2,
        y = center_y - height/2,
        width = width,
        height = height,
        **LAYERS["Metal3"]
    )

    # -----------------------------
    # Via2 definition (Option A)
    # -----------------------------

    VIA2_SIZE = 0.2          # um (side length of via)
    VIA2_SPACING = 0.5       # um (rule MIM.9) MIM.9 – Min. via spacing for sea of via on MIM top plate = 0.5 µm
    VIA2_EDGE_MARGIN = 0.4   # um (rules MIM.4 and MIM.5) 
    # MIM.4 – Minimum MiM top plate (FuseTop) overlap of Via2 = 0.4 um
    # MIM.5 – Minimum spacing between top plate and the Via2 connecting to the bottom plate = 0.4 um

    via_x_min = center_x - width/2 + VIA2_EDGE_MARGIN
    via_x_max = center_x + width/2 - VIA2_EDGE_MARGIN
    via_y_min = center_y - height/2 + VIA2_EDGE_MARGIN
    via_y_max = center_y + height/2 - VIA2_EDGE_MARGIN

    if via_x_min >= via_x_max or via_y_min >= via_y_max:
        raise ValueError("MIM too small to place Via2 respecting MIM.4/MIM.5 rules")

    vias = []

    x = via_x_min
    while x <= via_x_max:
        y = via_y_min
        while y <= via_y_max:
            vias.append(
                create_rectangle(
                    x = x - VIA2_SIZE/2,
                    y = y - VIA2_SIZE/2,
                    width = VIA2_SIZE,
                    height = VIA2_SIZE,
                    **LAYERS["Via2"]
                )
            )
            y += VIA2_SIZE + VIA2_SPACING
        x += VIA2_SIZE + VIA2_SPACING





