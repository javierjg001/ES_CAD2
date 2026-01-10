mim = create_mim_capacitor(
    width=10,
    height=8,
    option="A"
)

cap1 = create_mim_capacitor(10, 10, option="A")
cap2 = create_mim_capacitor(20, 5, option="B")

top.add(gdspy.CellReference(cap1, (0, 0)))
top.add(gdspy.CellReference(cap2, (30, 0)))

