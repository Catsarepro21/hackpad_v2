# hackpad_v2

A wireless six-key macropad with a Seeed XIAO ESP32-S3, two clickable rotary encoders, and twelve SK6812 MINI-E RGB LEDs. The simple version only powers on RGB when USB is connected, but the new parts can easily be added later.
![Macropad enclosure](images/Onshape-enclosure.jpg)

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


The latest STEP is exported from the current PCB and the case opening clears the slide-switch travel envelope. See [release audit](docs/Release-audit.md): electrical CAD checks pass; MX plate fit, socketed XIAO/USB clearance and firmware/hardware testing still prevent a production-qualified sign-off.

The [BOM](BOM.md) lists the 14 shopping lines plus all owned, DNP, jumper and mounting references. Prices are the saved October 16 cart; shipping, tax, PCB fabrication and printing are not a final delivered quote. [code/code.ino](code/code.ino) is the unchanged expander-based firmware and requires the direct-matrix changes described in the build instructions.
