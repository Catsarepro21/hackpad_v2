# Independent hardware review

Reviewed directly against the exported netlist, checked PCB, and manufacturer documentation after the external AI review was stopped at the user's request. No additional circuit change is required for the simple USB-only RGB population. This is a design review, not a powered prototype result.

## Confirmed

- The direct 2x4 matrix contains six keys and both encoder clicks. Its six matrix signals, four quadrature signals and one RGB data signal use eleven distinct XIAO GPIOs. Native USB uses its own pins. Scan by pulling one row low while reading columns with pull-ups; keep other rows high impedance. Both encoder common pins are grounded; enable input pull-ups and debounce in firmware.
- GPIO3's reset strap controls JTAG selection, not normal boot mode. Keep matrix rows high impedance during reset. D6/GPIO43 and D7/GPIO44 also serve UART0, so firmware must not drive the matrix column through UART TX after initialization.
- With the fourteen DNP parts absent, the only intentional supply connection to the LED/buffer 5V rail is VBUS through JP7. Battery power stays on the XIAO battery input. Seeed's v1.1 schematic shows separate USB and battery paths into its regulator; there is no intentional battery-to-VBUS supply path.
- U4's pin assignment matches TI: OE=1 grounded, A=2 on GPIO2, GND=3, Y=4 through330ohm to the first LED, VCC=5 on USB RGB5V. TI specifies input leakage up to1uA over VCC0-5.5V at its input test endpoints. This supports using the MCU input while the USB-powered buffer is off; measure actual off-state current on the assembled board.
- Q1/Q2 share their source and gate nodes, with the100k gate-to-source pull-up and switch/1k gate pull-down. This is the retained back-to-back battery disconnect. Off isolates the battery from both the XIAO load and charger; switch ON to charge. USB can still power the controller and LEDs with the battery switch off.
- The simple and full-upgrade jumper states pass explicit net-union checks. In the simple build MCU_D0/4/5 are isolated from RGB_EN/SDA/SCL. In the upgrade those functions reconnect and the direct extra matrix links open. JP7 must be opened before boost population.
- The optional TPS61023 pin mapping matches TI: FB1, EN2, VIN3, GND4, SW5, VOUT6. The732k/100k divider sets approximately4.992V. For a future boost build, verify effective output capacitance and transient stability: TI recommends feedforward compensation above40uF effective capacitance (about220pF across the732k resistor for a1kHz zero). This does not add a purchase or requirement to the simple build.

## Evidence and limits

KiCad10.0.6 reports0 ERC violations,0 PCB violations including warnings,0 unconnected items and0 schematic mismatches. All221 exported pin assignments match the PCB. All71 original footprints retain positions, rotations, layers and library IDs. Pushed manufacturing files match the local checked-file hashes.

Battery/body CAD interference checks pass for the stated envelopes. Flexible wires, connector polarity, antenna placement and printed tolerances remain assembly checks. The500mAh battery's500mA continuous rating applies to controller-only battery use, not an automatic approval for a later LED load. The unchanged expander firmware must be adapted for direct matrix scanning, and BLE/USB HID operation must be tested on hardware. Firmware was deliberately not modified.

Sources: [Seeed pin map and power information](https://wiki.seeedstudio.com/xiao_esp32s3_getting_started/), [Seeed v1.1 schematic](https://files.seeedstudio.com/wiki/SeeedStudio-XIAO-ESP32S3/res/XIAO_ESP32S3_SCH_v1.1.pdf), [TI AHCT buffer datasheet](https://www.ti.com/lit/ds/symlink/sn74ahct1g125.pdf), [TI TPS61023 datasheet, sections5 and8.2.2.4](https://www.ti.com/lit/ds/symlink/tps61023.pdf), [Adafruit battery datasheet](https://cdn-shop.adafruit.com/product-files/1578/Datasheet.pdf).
