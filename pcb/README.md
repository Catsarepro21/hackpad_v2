# Fabricate wireless macropad — PCB revision D

Six MX keys, two EC11E encoders with working push switches, and twelve SK6812 MINI-E LEDs. LED1–6 illuminate keys, LED7–8 illuminate encoders, LED9–12 are reserved for PCB edges. The OLED connector has been removed. The XIAO is centered between the encoders, with USB facing the top edge.

## Added circuitry

- MCP23008-E/P input expander, I2C address 0x20, for a 2-row by 4-column switch matrix. GP0/GP1 are ROW0/ROW1; GP2–GP5 are COL0–COL3. Enable column pull-ups; scan one row LOW and leave the other high impedance. Configure unused GP6/GP7 as outputs LOW. Encoder rotation remains directly connected to the XIAO.
- TPS61023DRL boost supply, nominal 5V, with 1uH inductor and 732k/100k feedback divider. L1 is the selected Bourns SRP5030T-1R0M. Ceramic capacitance must meet the converter requirements after DC-bias derating. Layout must follow TI guidance.
- Two SS34 Schottky diodes select USB VBUS or the switched LiPo for the RGB supply while blocking reverse current between sources.
- SN74AHCT1G125DBVR translates RGB data from 3.3V to 5V; 330-ohm series data resistor and one 100nF capacitor at each LED.

## Firmware and power

XIAO D0/GPIO1 = RGB enable, D1/GPIO2 = RGB data, D4/GPIO5 = SDA, D5/GPIO6 = SCL. Encoder1 A/B = D7/GPIO44 and D8/GPIO7. Encoder2 A/B = D9/GPIO8 and D10/GPIO9. Enable encoder input pull-ups and debounce clicks in firmware. The expander is polled; its interrupt is unused.

RGB enable has a hardware pull-down: lights default off. Hold data LOW before enabling power and send a clear frame before fading up. Begin at 25% brightness and validate the current budget against the actual USB source and LEDs. Twelve 12mA-per-channel LEDs can draw roughly 432mA at 5V on full white, excluding controller and converter losses. Select a protected 1S 3.7V LiPo rated for at least 1.5A continuous discharge; confirm capacity, dimensions, polarity and charging compatibility before ordering. Do not assume all-white operation fits a 500mA USB port.

SW7 disconnects the battery, including charging. The switch controls a common-source AO3401A MOSFET pair through a1k gate resistor; a100k gate-to-source resistor defaults it off. With USB connected, the pad and RGB supply can still operate. Charging is through the XIAO; no separate charger is added. Firmware battery-level monitoring is not included.

## PCB and assembly

The board is placed and routed: 84 x 78 mm, two copper layers, 1.6 mm FR-4, 3 mm corner radius. The six switch centers use 19.05 mm pitch in both directions. Four 3.2 mm M3 mounting holes are at (55,73), (127,73), (55,139), (127,139) mm in the KiCad drawing. The board spans X=48..132 and Y=66..144 mm. No explanatory text was added to the schematic or PCB.

MX switches, encoders and XIAO sockets mount on the front. J1 battery connector mounts on the rear at (76,72) mm. Diodes, input expander, RGB circuitry and LEDs mount on the back. SK6812 MINI-E LEDs face through the supplied board cutouts: one at each key's south LED position, one beside each encoder's lower edge, and four around the perimeter. The encoder bodies are opaque; their LEDs require an enclosure diffuser/gap. Key illumination depends on switch-housing transparency and the actual housing opening. Solid keycaps primarily show light around their edges.

U1 uses two seven-position 2.54 mm sockets/headers, with 15.24 mm row separation. Header geometry was checked against Seeed's official S3 footprint. The two extra BAT+ and BAT- holes on the carrier are wire attachment points, not direct module contacts: solder short wires to the XIAO's underside battery pads before installing it in the sockets. USB faces the top edge. Keep the supplied external antenna away from copper, battery and metal; mount it in the enclosure outside the board area when practical.

J1 is a JST-PH B2B-PH-K vertical connector: pin 1 is battery positive and pin 2 is ground. Confirm battery-plug polarity before connecting. SW7 is a C&K JS102011SAQN right-angle slide switch. L1 is a Bourns SRP5030T-1R0M. U4 is SN74AHCT1G125DBVR, SOT-23-5. U3 is TPS61023DRLR, SOT563; plan a suitable reflow process for this small part. The carrier socket strips, battery, power switch, connector, capacitors, resistors, Schottky diodes, inductor and three added ICs are new purchases.

KiCad electrical rules, PCB design rules, connectivity, and schematic parity were checked. The design has not been built or bench tested. Before ordering, compare a 1:1 print with the recovered parts, select a protected battery that meets the discharge rating, and design the enclosure/battery tray with clearance for the rear-mounted DIP IC and components. These mechanical and physical checks cannot be replaced by DRC.

Manufacturer references: https://www.ti.com/lit/ds/symlink/tps61023.pdf ; https://www.ti.com/product/SN74AHCT1G125 ; https://cdn-shop.adafruit.com/product-files/4960/4960_SK6812MINI-E_REV02_EN.pdf

Revision B: removed J2/OLED; moved XIAO to (91,79) mm between encoder shafts at (70,80) and (113.5,80) mm. Moved battery connector to (57,88) mm, reorganized rear power circuitry, and rerouted the compact board. Key pitch remains 19.05 mm; all twelve RGB LEDs and both encoder clicks remain. Electrical checks and schematic/PCB parity pass with no violations or unconnected items.

Revision D: added Q1/Q2 AO3401A, R9 100k and R10 1k to remove battery load from the0.3A switch. Internal rear JST replaces exposed top connector, and the cover opening is closed. C4/C5 selected22uF16VX7R1210. Battery reference is SparkFun PRT-26059, with54x37x9mm CAD clearance envelope. See BOM.md and Engineering-review.md for costs, qualification limits and remaining firmware/bench work.

