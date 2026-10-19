# hackpad_v2

A wireless six-key macropad with a Seeed XIAO ESP32-S3, two clickable rotary encoders, and twelve SK6812 MINI-E RGB LEDs. The simple version only powers on RGB when USB is connected, but the new parts can easily be added later.
![Earlier Onshape enclosure reference](images/Onshape-enclosure.jpg)

*Earlier reference image; use the local STEP/STL files for the corrected case.*

## Files

| Folder | Contents |
| --- | --- |
| [case](case/) | Separate base and cover STEP files, plus a combined case STEP |
| [pcb](pcb/) |  KiCad project |
| [manufacturing](manufacturing/) | Gerber and drill files ZIP |

### Downloads

- [Base STEP](case/Base_tray.step)
- [Cover STEP](case/MX_switch_plate.step)
- [Combined case STEP](case/Hackpad_V2_case.step)
- [Earlier Onshape reference (local STEP/STL files contain the current corrections)](https://cad.onshape.com/documents/e5e00bd96b00b1f98fd3bff8/w/d80bdedc56342f5387c6fe9a/e/5cf3044721cd9ba3212c3cf5?renderMode=0&uiState=6ad18d197901a43b19ded2cc)
- [PCB STEP](pcb/Fabricate_Wireless_Macropad.step)
- [Gerber/drill ZIP](manufacturing/Gerbers-and-drills.zip)
- [BOM](BOM.md) / [CSV](BOM.csv)
- [Build and upgrade jumper settings](pcb/Build-options.md)
- [Verification and remaining hardware checks](pcb/Verification.md)
- [Printable base](case/Base_tray.stl) / [plate](case/MX_switch_plate.stl)


The PCB STEP is exported from the current native PCB. The corrected 1.5 mm plate spans z=5.1–6.6 mm above the PCB-bottom datum, and the case is 90 x 84 x 25.0 mm. Model origins and the nominal socketed XIAO height were corrected. See the [case notes](case/README.md) and [release audit](docs/Release-audit.md): exact owned-part fit, header seating, USB cable access and hardware/firmware testing still prevent a production-qualified sign-off.

The [BOM](BOM.md) lists the 14 shopping lines plus all owned, DNP, jumper and mounting references. Prices are the rebuilt October 17 cart; shipping, tax, PCB fabrication and printing are not a final delivered quote. [code/code.ino](code/code.ino) is the unchanged expander-based firmware and requires the direct-matrix changes described in the build instructions.
