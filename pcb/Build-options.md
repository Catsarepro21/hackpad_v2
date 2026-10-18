# Population and solder jumpers

All original component footprints remain, including U2 MCP23008-E/SO and the TPS61023 battery RGB supply. Optional does not mean disconnected by default: use the jumper configuration below.

| Jumper | Simple build now | Full upgrade later |
|---|---|---|
| JP1 | Bridge pads 2-3: D0 to ROW0 | Bridge 1-2: D0 to RGB_EN |
| JP2 | Closed: D2 to ROW1 | Open |
| JP3 | Closed: D3 to COL0 | Open |
| JP4 | Bridge 2-3: D4 to COL1 | Bridge 1-2: D4 to SDA |
| JP5 | Bridge 2-3: D5 to COL2 | Bridge 1-2: D5 to SCL |
| JP6 | Closed: D6 to COL3 | Open |
| JP7 | Closed: USB VBUS to RGB 5V | OPEN before installing battery RGB parts |

Never bridge both sides of a three-pad jumper. Disconnect USB and battery before changing jumpers. Remove JP7's bridge before populating U3/D9/D10 and the boost circuit: leaving it closed defeats the original supply isolation.

Leave these 14 references unpopulated now: U2, R1, R2, R3, C2, U3, L1, D9, D10, C3, C5, R4, R5, R6. Native schematic and PCB DNP flags mark them. Keep C4 as USB RGB bulk capacitance. Keep U4, R7, R8 and C6 for a proper 3.3V-to-5V RGB signal. Keep Q1/Q2 and SW7 for the existing battery disconnect.

## Firmware interface (firmware not edited)

| Function | XIAO label | ESP32 GPIO |
|---|---|---:|
| ROW0 | D0 | 1 |
| ROW1 | D2 | 3 |
| COL0 | D3 | 4 |
| COL1 | D4 | 5 |
| COL2 | D5 | 6 |
| COL3 | D6 | 43 |
| Encoder 1 A/B | D7 / D8 | 44 / 7 |
| Encoder 2 A/B | D9 / D10 | 8 / 9 |
| RGB data | D1 | 2 |

Encoder clicks remain in the 2x4 matrix alongside the six keys. Retain the original diode orientation. GPIO3 is a strap pin affecting JTAG selection; keep matrix rows high impedance through reset. Native USB uses separate pins.

The old MCP23008 scanner will not operate the direct matrix unchanged. Implement direct scanning using this table and verify BLE/USB HID on hardware. Bluetooth support in the existing firmware has not been confirmed. Keep Wi-Fi off on the 500mAh battery. RGB works only with USB power in the simple build; start at brightness 64/255 and measure USB current before raising it, including charging current in the USB power budget.

For the full upgrade populate all 14 optional references with their original values/footprints, reconfigure jumpers, and restore the expander scanner and RGB enable control. Reassess battery discharge capacity before enabling battery RGB; the smaller 500mAh pack is not automatically qualified for that load.

Sources: [Seeed pin map](https://wiki.seeedstudio.com/xiao_esp32s3_getting_started/), [LED supply requirements](https://cdn-shop.adafruit.com/product-files/4960/4960_SK6812MINI-E_REV02_EN.pdf), [AHCT buffer](https://www.ti.com/lit/ds/symlink/sn74ahct1g125.pdf).

## Finding the jumpers

Read the board from its underside, with the USB connector at the top. All jumpers have the same orientation: pad 1 is on the left; for three-pad jumpers pad 2 is the center and pad 3 the right. Use the reference labels and the native PCB assembly view to identify them; verify continuity before applying power.

## Power and scanning notes

Switch ON to charge the battery: SW7 disconnects the battery from both controller and charger when off. USB still powers the controller and RGB with the battery switch off. For matrix scanning, read columns with pull-ups and drive one row low at a time, leaving other rows high impedance. Disable UART0 TX on GPIO43 before using it as a column input. See the [release audit](../docs/Release-audit.md) for remaining validation. For a future boost build, check effective output capacitance and transient response: TI recommends feedforward compensation above 40uF effective capacitance (approximately 220pF across the 732k upper feedback resistor for a 1kHz zero); this is not required for the simple DNP boost population.
