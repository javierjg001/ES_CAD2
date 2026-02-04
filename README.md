# CAD2 Porting PDK 180nm Global Foundries
### *Parametric layout generator for the GlobalFoundries 180 nm MCU PDK*  
**Embedded Systems – CAD2 Project (Analog Layout Automation)**  
***Politecnico di Milano***

---

## Project Overview

This repository contains a **parametric generator for a MIM (Metal–Insulator–Metal) capacitor** targeting the **GlobalFoundries GF180MCU technology**.  
The generator is implemented in **Python using gdspy**, with the purpose of creating **rule-compliant layouts automatically**, following the specifications of the **GF180 MCU Design Rule Manual (DRM), Section 10.4 – MIM Capacitors**.

The project is part of the **Embedded Systems course (Politecnico di Milano)**.

---

## Project Supervisors
- **Dott. Giuseppe Chiari**  
- **Dott. Michele Piccoli**  
- **Prof. Davide Zoni**  

---

## Project Goals

**Implementation of GlobalFoundries GF180MCU PDK Design Rules**

Analog layout design automation is increasingly important to accelerate analog IC development.  
This project contributes to this direction by providing **parametric and customizable procedures for the automatic generation of MIM capacitor layouts**, supporting both **Option A and Option B** as defined in the GlobalFoundries GF180MCU PDK.

---

## Specific Objectives of This Repository

- Study the **MIM capacitor structure and design rules** in GF180 (DRM 10.4).
- Implement **parametric geometry generation** using gdspy.
- Verify and enforce:
  - minimum width and height  
  - minimum area  
  - enclosure rules between plates  
  - spacing to other layers  
  - via placement constraints  
- Produce a **GDSII layout output** of the generated capacitor.

---

## Repository Structure
```text
ES_CAD2/
│
├── src/               # Python parametric generator scripts (gdspy)
├── gds/               # Generated GDSII layouts
└── README.md          # Project documentation
```

## Author  
**Javier González Santamaría**  
Embedded Systems – A.Y. 2025  
Politecnico di Milano
