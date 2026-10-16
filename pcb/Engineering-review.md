# Wireless macropad engineering review — revision D

Reviewed 15 October 2026. The revised prototype design passes the recorded software checks. It is **not a proven working macropad**: no new parts have been purchased, no board has been built, and firmware is not written.

## Changes from the earlier design

- The JS102011SAQN slide switch is rated 0.3 A. The battery load could exceed this, so it now controls two AO3401A P-channel MOSFETs instead of carrying the load directly. Q1/Q2 share sources and gates, with a 100 kΩ source-to-gate pull-up and 1 kΩ switch-to-gate resistor. This permits charging/discharging when on and blocks both directions when off. The gate resistor limits switch gate current; it is not a validated battery inrush limiter.
- J1, the battery JST-PH connector that protruded through the top, now mounts on the rear at PCB coordinates (76,72) mm. Its cover opening is closed. It remains a battery connector; it is not an external accessory port.
- The battery guide spacing now allows a 54 × 37 × 9 mm clearance envelope for the selected protected SparkFun PRT-26059 pack. Its drawing specifies a pack 51 ±1 × 34 ±0.5 × 7.8 ±0.3 mm, including the folded protection-board construction. Wire routing, swelling allowance and the actual received pack still require physical confirmation. The guide ends are open for the leads.
- Output capacitors C4/C5 are specified as Samsung CL32B226KOJNFNE, 22 µF, 16 V, X7R, 1210. The 16 V rating replaces the earlier generic 10 V parts.

## Three verification passes

1. **Native connectivity and rule checks:** KiCad ERC reports zero violations. PCB DRC reports zero violations, zero unconnected items and zero schematic-parity issues. A separate comparison checks every numbered PCB pad against the native schematic XML netlist. Six switch centers retain 19.05 mm pitch. Manufacturing files were re-exported from this revision.
2. **Manufacturer/pin review:** XIAO header GPIO assignments, MCP23008 PDIP-18, TPS61023 DRL, AHCT125 DBV, MOSFET G/S/D and diode polarity were compared with their documentation. The six keys and two encoder clicks form a two-row/four-column matrix; both encoder rotations remain direct MCU inputs. Twelve LEDs have a continuous data chain. The MINI-E footprint uses KiCad numbering that differs from the manufacturer's numbering: the physical reverse-mount pad positions, including the marked ground corner, were compared rather than assuming matching pin numbers.
3. **Independent Gemini Argon critique:** The actual netlist, package choices, physical LED/switch coordinates, corrected disconnect circuit and priced BOM were discussed in multiple rounds in the existing Brave Gemini tab. Gemini agreed with the corrected common-source MOSFET topology and highlighted minimum-order costs, salvage testing, assembly tools, battery dimensions and bench testing. Its responses are a second opinion, not a measurement or fabrication certification.

Gemini initially claimed an incorrect switch pin swap, imported specifications from other TI converters, and overstated GPIO44 boot risk. These were challenged with physical coordinates and primary documents and retracted. Its initial claim that the RGB load must pass through an internal USB/header diode does not match the inspected regular XIAO S3 V1.3 schematic: both the USB connector and 5 V header use VBUS; D2 feeds the internal VIN regulator path. Do not use those earlier model claims as design authority.

## CAD checks

The base and cover are each one valid solid, with zero mutual overlap. Dimensions remain 90 × 84 × 23.4 mm around the 84 × 78 mm PCB. The updated component-reference STEP, including the rear JST and added SOT-23 parts, has zero positive-volume interference with either case solid. A 54 × 37 × 9 mm battery clearance box has zero modeled interference. All six reference keycaps clear a full 4 mm downward stroke. Existing M3 heat-set pockets and screw axes are unchanged; their prior geometric checks remain applicable.

The cover supports PCB-mounted switches; it does not latch their plate clips. The MX switch body uses a simplified dimensional envelope because the detailed third-party model had unsuitable positioning. Reference geometry and static CAD do not establish exact physical socket, connector, keycap or knob fit. Onshape previously reported translation faults in some third-party component references; the printable case solids validate independently. Print a fit prototype and heat-set hole coupon.

## Remaining checks before calling the hardware finished

- **Matrix voltage margin:** MCP23008's guaranteed input-low limit is 0.2 × VDD, or 0.66 V at 3.3 V. The actual 1N4148 forward drop plus row output voltage must remain below that under the real weak pull-up current and intended temperatures. Retaining owned silicon diodes is a cost-saving choice, not a worst-case guarantee. If measurements lack margin, DO-35 BAT42 replacements need to be qualified before populating the matrix. Test simultaneous presses and both encoder clicks.
- **Boost layout and stability:** The 732 kΩ/100 kΩ divider, 1 µH inductor and 10 µF input/two 22 µF output values match TI's reference circuit. PWM nominal output is 0.595 × 8.32 = 4.9504 V. Verify the selected capacitors' effective capacitance at operating DC bias; TI recommends feedforward compensation when effective output capacitance exceeds 40 µF. The converter is a boost/pass-through device, not a buck regulator. Scope startup, ripple, load transitions and switch-node behavior. DRC cannot validate analog stability or EMI; the feedback path and power loop warrant bench attention.
- **Power and USB budget:** Twelve nominal 12 mA-per-channel LEDs can use approximately 432 mA for their channels on full white, plus idle current. Controller, converter losses and charging add load. Start with RGB limited to 25% and measure actual source current; no assurance is made that full white fits a 500 mA USB source. Verify low-battery transients, MOSFET/diode/inductor temperature and protected-cell inrush behavior.
- **Charging and module revision:** The regular S3 wiki describes 50 mA fast charging, while Seeed's V1.3 schematic labels approximately 110 mA with a 220 kΩ programming resistor. Confirm the received board revision; a 1500 mAh pack can therefore take many hours to charge. A separate charger is not required. The selected pack permits 750 mA maximum charging and 1.5 A continuous discharge. Charging is deliberately disconnected when SW7 is off.
- **Assembly:** Inspect JST plug polarity with a meter, insulate the underside battery leads, and allow service slack beneath the socketed XIAO. The SOT-563 boost chip requires suitable fine-pitch assembly equipment/technique. Test recovered encoders and LEDs before installation; the original kit's sixteen LEDs do not establish that twelve unused LEDs remain.
- **Firmware and radio:** Implement matrix scanning, pull-ups, debouncing, encoder decoding, GRB LED timing/power sequencing, USB HID and BLE HID. No interrupt wake trace is added in revision D; the expander is polled. No battery-level sensing is provided. Test reset with both encoder states, actual sleep current, reconnect behavior and external antenna placement.

## Primary references

- [Littelfuse/C&K JS series](https://www.littelfuse.com/products/switches/slide-switches/js)
- [AO3401A manufacturer datasheet](https://www.aosmd.com/pdfs/datasheet/AO3401A.pdf)
- [TI TPS61023 datasheet](https://www.ti.com/lit/ds/symlink/tps61023.pdf)
- [TI SN74AHCT1G125 datasheet](https://www.ti.com/lit/ds/symlink/sn74ahct1g125.pdf)
- [Microchip MCP23008/MCP23S08 datasheet](https://ww1.microchip.com/downloads/aemDocuments/documents/APID/ProductDocuments/DataSheets/MCP23008-and-MCP23S08-Data-Sheet-DS20001919.pdf)
- [Opsco MINI-E Rev02 datasheet](https://cdn-shop.adafruit.com/product-files/4960/4960_SK6812MINI-E_REV02_EN.pdf)
- [Seeed regular S3 V1.3 schematic](https://files.seeedstudio.com/wiki/SeeedStudio-XIAO-ESP32S3/res/XIAO_ESP32S3_V1.3_SCH_260115.pdf), [Seeed wiki](https://wiki.seeedstudio.com/xiao_esp32s3_getting_started/)
- [Selected battery pack drawing/specification](https://cdn.sparkfun.com/assets/c/1/6/c/f/LP783450_1500mAh_with_connector_.pdf)

See BOM.md/BOM.csv for the purchasing budget and explicit exclusions. The saved Gemini transcript contains model-generated claims, including superseded errors; this report records the design conclusions and evidence boundaries.

The final BOM critique checked the $35.00 listed-price subtotal plus $6.80 allowances = $41.80 before shipping/tax. Its useful final correction was to consolidate suppliers: visiting every linked shop separately can exceed the $55–75 planning allowance. Exact shipping, tax, tariff and commercial assembly/printing costs remain unknown. Its suggested capacitor retention percentages were not independently verified and are not used as validated data.
