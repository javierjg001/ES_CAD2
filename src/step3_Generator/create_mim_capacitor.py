def create_mim_capacitor(
    width, #um^2
    height, #um^2
    option="A", #A or B
    center=(0, 0)):

    import gdspy
    from ..step2_Parametric.functions import (
    create_rectangle,
    offset_shape)


    LAYERS = {
    "FuseTop":  {"layer": 75, "datatype": 0},
    "Metal2":   {"layer": 36, "datatype": 0},
    "Metal3":   {"layer": 42, "datatype": 0},
    "Metal5":   {"layer": 81, "datatype": 0},
    "MetalTop": {"layer": 53, "datatype": 0},
    "CAP_MK":   {"layer": 117, "datatype": 5},
    "MIM_L_MK": {"layer": 117, "datatype": 10},
    "Via2":     {"layer": 38, "datatype": 0},
    "Via5":     {"layer": 82, "datatype": 0}
    }

    if option == "A":
        TOP_METAL = "Metal3"
        BOTTOM_METAL = "Metal2"
        VIA = "Via2"

    elif option == "B": # n = 6 since the LVP provided by the professor shows Metal1–Metal5 plus a distinct MetalTop layer, which defines the top metal for MIM Option B.
        TOP_METAL = "MetalTop"
        BOTTOM_METAL = "Metal5"
        VIA = "Via5"

    else:
        raise ValueError("Invalid MIM option")

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
    metal_bottom = offset_shape(fuseTop, distance=0.6, **LAYERS[BOTTOM_METAL])
    
    # HERE ARE TWO POSSIBLE APPROACHES FOR THE CAP_MK LAYER:
    # 1) Simple approach: CAP_MK coincident with FuseTop area
    # FuseTop enclosure by CAP_MK = 0, rule MIM.7
    #cap_mk = create_rectangle(
    #     x = center_x - width/2,
    #     y = center_y - height/2,
    #     width = width,
    #     height = height,
    #     **LAYERS["CAP_MK"]
    # )

    # 2) Second approach: adding an offset to the CAP_MK layer so it's larger than the FuseTop area
    # ADDING THE OFFSET APPROACH FOR CAP_MK TO COMPLY WITH RULE MIM.7
    #  Fusion Top enclosure by CAP_MK = 0.6 um (so it's same as the bottom metal offset)
    d_Cap_Top = 0.6  # um (enclosure distance for CAP_MK)
    # FuseTop enclosure by CAP_MK = 0, rule MIM.7
    cap_mk = offset_shape(fuseTop, distance=d_Cap_Top, **LAYERS["CAP_MK"])

    # MIM_L_MK to identify capacitor length, rule MIM.12
    MIM_L_MK_THICKNESS = 0.2  # um (marker thickness)

    if width >= height:
        # Length along X (width), marker at bottom edge
        mim_l_mk = create_rectangle(
            x = center_x - width/2,
            y = center_y - height / 2,  # bottom edge
            width = width,
            height = MIM_L_MK_THICKNESS,
            **LAYERS["MIM_L_MK"]
        )
    else:
        # Length along Y (height), marker at right edge
        mim_l_mk = create_rectangle(
            x = center_x + width / 2 - MIM_L_MK_THICKNESS,  # right edge
            y = center_y - height/2,
            width = MIM_L_MK_THICKNESS,
            height = height,
            **LAYERS["MIM_L_MK"]
        )

    # Top metal plate (coincident with FuseTop area)
    metal_top = create_rectangle(
        x = center_x - width/2,
        y = center_y - height/2,
        width = width,
        height = height,
        **LAYERS[TOP_METAL]
    )

    # -----------------------------
    # Via definition
    # -----------------------------

    VIA_SIZE = 0.2          # um (side length of via)
    VIA_SPACING = 0.5       # um (rule MIM.9) MIM.9 – Min. via spacing for sea of via on MIM top plate = 0.5 µm
    VIA_EDGE_MARGIN = 0.4   # um (rules MIM.4, MIM.5 and MIM.2) 
    # MIM.4 – Minimum MiM top plate (FuseTop) overlap of Via2 = 0.4 um
    # MIM.5 – Minimum spacing between top plate and the Via2 connecting to the bottom plate = 0.4 um

    via_x_min = center_x - width/2 + VIA_EDGE_MARGIN
    via_x_max = center_x + width/2 - VIA_EDGE_MARGIN
    via_y_min = center_y - height/2 + VIA_EDGE_MARGIN
    via_y_max = center_y + height/2 - VIA_EDGE_MARGIN


    # Check if there is enough space to place at least one Via2
    if via_x_min >= via_x_max or via_y_min >= via_y_max:
        raise ValueError("MIM too small to place Via2 respecting MIM.4/MIM.5 rules")

    vias = []

    x = via_x_min
    while x <= via_x_max:
        y = via_y_min
        while y <= via_y_max:
            vias.append(
                create_rectangle(
                    x = x - VIA_SIZE/2,
                    y = y - VIA_SIZE/2,
                    width = VIA_SIZE,
                    height = VIA_SIZE,
                    **LAYERS[VIA]
                )
            )
            y += VIA_SIZE + VIA_SPACING
        x += VIA_SIZE + VIA_SPACING

    cell = gdspy.Cell(f"MIM_{option}_{width}x{height}")

    cell.add(fuseTop)
    cell.add(metal_bottom)
    cell.add(cap_mk)
    cell.add(mim_l_mk)
    cell.add(metal_top)

    for v in vias:
        cell.add(v)

    return cell
