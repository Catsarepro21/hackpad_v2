# Corrected hackpad case

Use these local STEP/STL files for the current case. The Onshape image/link in the repository is an earlier reference.

| Dimension / datum | Nominal value |
|---|---|
| Overall case, excluding components protruding above it | 90 x 84 x 25.0 mm |
| PCB outline and thickness | 84 x 78 x 1.6 mm |
| PCB bottom / top z | 0 / 1.6 mm |
| Plate bottom / top z | 5.1 / 6.6 mm |
| Plate thickness | 1.5 mm |
| Integral spacers above PCB top | 3.5 mm |
| Space below PCB | 16 mm |
| Battery reserve | 40 x 33 x 7 mm |
| Battery envelope | 36 x 29 x 4.75 mm |

The XY outline and mounting coordinates are retained; the corrected plate raises the case top 1.6 mm above the previous version. The wire-access slot spans both carrier BAT pads. The switch opening accommodates the conservative slide-switch travel envelope. See the [release audit](../docs/Release-audit.md) and generated JSON reports for nominal-model checks and remaining limits.

The model uses a nominal 11.04 mm gap from carrier-board top to XIAO PCB underside: manufacturer-verified 8.50 mm female-socket housing plus assumed 2.54 mm male-header plastic. Measure the exact purchased header, confirm full seating and check an actual USB plug/cable. This nominal envelope does not qualify the exact mated stack.

Use Base_tray.step and MX_switch_plate.step as separate editable solids; Hackpad_V2_case.step combines the case, and Hackpad_V2_complete.step/Hackpad_V2_exploded.step include the PCB/component reference. Base_tray.stl and MX_switch_plate.stl are placed on the print bed by enclosure_source.py, with the tray floor and plate's flat outer face down. Check orientation in the slicer.

Assembly uses the owned four M3x16 screws and four 5 mm OD x 4 mm heat-set inserts. Check printed holes and insert retention before tightening. Print a plate sample with an actual owned MX switch before a final batch: the model is approximate and retains slight plate engagement. Confirm encoder footprint/shaft dimensions, battery restraint and wire routing, antenna placement, and USB/switch access in the first assembly. Avoid compressing the battery. The corrected CAD is not a production-qualified physical assembly.

The optional [MX fit coupon](Optional_MX_fit_coupon.md) tests the actual switch and printing process. [Measured CAD assumptions and remaining fit limits](../docs/CAD-correction-report.md) accompany the geometry.
