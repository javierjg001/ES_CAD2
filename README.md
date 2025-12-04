# GF180 MIM Capacitor Generator  
### Parametric layout generator for the GlobalFoundries 180nm MCU PDK (Analog CAD Project)

This repository contains a **parametric generator of a MIM (Metal–Insulator–Metal) capacitor** for the **GlobalFoundries GF180MCU process**.  
The project is developed as part of the **Embedded Systems course (Politecnico di Milano)**, under the **CAD2 – Analog Layout Automation** project track.

The goal is to automatically generate the layout of a MIM capacitor while ensuring that all geometrical constraints defined in the **GF180 MCU Design Rule Manual (DRM), Section 10.4** are satisfied.

---

## Project Objectives

- Understand the structure and technology of the **MIM capacitor** in the GF180 PDK.
- Build a **parametric layout generator** using **Python + gdspy**.
- Implement **rule-checking logic** according to the DRM:
  - Minimum width and height  
  - Minimum area  
  - Enclosure rules between plates  
  - Minimum spacing to other layers  
  - Allowed shapes and via placement rules  
- Export the final design in **GDSII** format.
- Provide a reproducible and verifiable layout automation workflow.

### Javier González Santamaría
Politecnico di Milano
Embedded Systems — CAD2 Project (Analog Layout Automation)