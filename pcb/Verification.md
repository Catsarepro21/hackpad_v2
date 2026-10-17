# Verification of simple build with upgrade pads

KiCad 10.0.6: zero reported DRC violations (including warnings), zero unconnected items, zero schematic parity issues; ERC zero reported violations. Reports in ../docs preserve the configured ignored checks for transparency. Existing LED aperture and fine-pitch converter clearance rules are retained; general clearances were not relaxed to pass.

All 71 original footprints retain their library ID, position, rotation and PCB side. Seven solder jumpers were added. All 221 netlisted pin connections match the PCB. Fourteen optional references carry DNP flags in both schematic and PCB. Logical checks passed for both jumper configurations; these checks do not simulate the components or replace electrical measurements.

The Gerber/drill ZIP was exported from this checked board and includes both copper, paste, silkscreen and mask layers, board edges, and separate plated/nonplated drill files. All optional copper pads are present for later assembly.

Battery CAD: valid single-solid tray and plate; zero tray/plate intersection. The 36x29x4.75mm battery envelope has zero interference with tray or plate. Its 40x33x7mm reserved volume has zero interference with the original fully populated PCB mechanical reference. The guide spacing is 40.2mm. Mounting locations and case exterior are unchanged. Flexible leads, adhesive/foam restraint, printed tolerance, antenna placement, USB/switch access and full assembly fit require physical verification. The new solder jumpers are flat copper and are not modeled in the STEP reference.

Firmware was not modified. The old MCP23008 scanner requires adaptation for the direct matrix, and BLE HID operation remains unverified in hardware. Start RGB at brightness 64/255, keep Wi-Fi off on battery, and measure supply current before increasing brightness. Verify battery connector polarity before connection. Future battery RGB needs the JP7 bypass opened and battery discharge capacity checked.

See [independent component and power review](../docs/Self-review.md) for the manual manufacturer cross-check.
