# hackpad_v2

A wireless six-key macropad with a Seeed XIAO ESP32-S3, two clickable rotary encoders, and twelve SK6812 MINI-E RGB LEDs. Revision D uses 19.05 mm key spacing and an internal battery connector.

![Macropad enclosure](images/Onshape-enclosure.jpg)

## Files

| Folder | Contents |
| --- | --- |
| [case](case/) | Separate base and cover STEP files, plus a combined case STEP |
| [pcb](pcb/) | Editable KiCad project, schematics, custom libraries, reference models and assembled PCB STEP |
| [manufacturing](manufacturing/) | Gerber and separate plated/non-plated drill files ZIP |
| [docs](docs/) | Engineering review and KiCad check reports |

Open `pcb/Fabricate_Wireless_Macropad.kicad_pro` in KiCad 10. The project includes its custom symbol/footprint library and referenced local models. Standard component models use KiCad's installed 3D library.

### Downloads

- [Base STEP](case/Base_tray.step)
- [Cover STEP](case/MX_switch_plate.step)
- [Combined case STEP](case/Hackpad_V2_case.step)
- [PCB STEP](pcb/Fabricate_Wireless_Macropad.step)
- [Gerber/drill ZIP](manufacturing/Gerbers-and-drills.zip)
- [BOM](BOM.md) / [CSV](BOM.csv)

## Status

Native ERC, PCB DRC, connectivity and schematic parity passed with no reported violations. The modeled case and battery clearance checks passed. This is an unbuilt prototype: firmware, real-part fit, soldering, power/charging measurements and USB/Bluetooth operation still require validation. See the [engineering review](docs/Engineering-review.md) for limitations and remaining checks.

The cover supports PCB-mounted switches; it is not a switch clip plate. Heat-set insert pockets target M3 inserts, nominal 5 mm outside diameter and 4 mm long; print a fit coupon. Third-party component visuals are references, not exact manufacturing geometry.
