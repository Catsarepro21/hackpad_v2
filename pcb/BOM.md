# Wireless macropad — parts and purchasing budget

Revision D • USD • checked 15 October 2026 • no parts purchased

**Budgeted parts, minimum buy quantities and printing: $41.80 before shipping/tax.** Of this, $35.00 comes from listed prices; $6.80 is explicitly estimated. This is not a delivered checkout quote. Existing parts have $0 additional cost, not $0 replacement value.

For planning, reserve **about $55–75 delivered** if tools and printer access are already available. This is an allowance, not a shipping/tax quote. Separate vendors, battery ground shipping and tariffs can change it. Commercial printing or buying soldering equipment is extra.

## Already owned or recovered

| Item | Required | Additional cost | Notes |
|---|---:|---:|---|
| MX-style PCB switches | 6 | $0 | Six spare switches; brand/model unspecified. Compare physical pins to footprint. |
| White blank DSA MX keycaps | 6 | $0 | Opaque: light mainly around cap edges, depends on switch housing. |
| 1N4148 DO-35 | 8 | $0 | Count eight usable diodes; cathode stripe to row. Test matrix low voltage. |
| EC11E with push switch | 2 | $0 | Test A/C/B contacts and both pushbuttons after removal; do not assume Alps brand. |
| SK6812 MINI-E reverse mount | 12 | $0 | Kit had16 total. If old pad used6, only10 loose remain; recover2 or buy spares. Test full data chain. |
| M3x16 screws | 4 | $0 |  |
| M3 brass heat-set; 5mm OD x4mm long | 4 | $0 | 4.6mm CAD pilot holes need print-fit coupon. |

## New parts / minimum purchase quantities

| Ref | Selected part | Used / buy | Purchase USD | Basis / source |
|---|---|---:|---:|---|
| U1 | Seeed XIAO ESP32-S3 113991114 (regular) | 1 / 1 | $7.49 | Listed price; [source](https://www.seeedstudio.com/XIAO-ESP32S3-p-5627.html) |
| U2 | Microchip MCP23008-E/P PDIP-18 | 1 / 1 | $1.81 | Listed price; [source](https://www.lcsc.com/product-detail/C646745.html) |
| U3 | TI TPS61023DRLR SOT-563 | 1 / 5 | $1.34 | Listed price; [source](https://www.lcsc.com/product-detail/C919459.html) |
| U4 | TI SN74AHCT1G125DBVR SOT-23-5 | 1 / 5 | $0.51 | Listed price; [source](https://www.lcsc.com/product-detail/C7484.html) |
| Q1,Q2 | AOS AO3401A P-channel SOT-23 | 2 / 10 | $0.59 | Listed price; [source](https://www.lcsc.com/product-detail/C15127.html) |
| SW7 | C&K JS102011SAQN | 1 / 1 | $0.87 | Listed price; [source](https://www.lcsc.com/product-detail/C221660.html) |
| L1 | Bourns SRP5030T-1R0M 1uH | 1 / 1 | $1.10 | Budget estimate; current qty1 price not confirmed; [source](https://www.digikey.com/en/products/detail/bourns-inc/SRP5030T-1R0M/3986079) |
| D9,D10 | MDD SS34 SMA | 2 / 20 | $0.70 | Listed price; [source](https://www.lcsc.com/product-detail/C8678.html) |
| C1,C2,C6–C18 | Yageo CC0805KRX7R9BB104 100nF50VX7R0805 | 15 / 20 | $0.38 | Listed price; [source](https://www.lcsc.com/product-detail/C49678.html) |
| C3 | KEMET C1206C106K8RACTU 10uF10VX7R1206 | 1 / 5 | $0.66 | Listed price; [source](https://www.lcsc.com/product-detail/C2167669.html) |
| C4,C5 | Samsung CL32B226KOJNFNE 22uF16VX7R1210 | 2 / 5 | $1.40 | Listed price; [source](https://www.lcsc.com/product-detail/C16196563.html) |
| R1,R2 | UNI-ROYAL 0805W8F4701T5E 4.7k1% | 2 / 100 | $0.51 | Listed price; [source](https://www.lcsc.com/product-detail/C17673.html) |
| R3 | UNI-ROYAL 0805W8F1002T5E 10k1% | 1 / 100 | $0.34 | Listed price; [source](https://www.lcsc.com/product-detail/C17414.html) |
| R4 | UNI-ROYAL 0805W8F7323T5E 732k1% | 1 / 100 | $0.29 | Listed price; [source](https://www.lcsc.com/product-detail/C17816.html) |
| R5,R6,R8,R9 | UNI-ROYAL 0805W8F1003T5E 100k1% | 4 / 100 | $0.60 | Listed price; [source](https://www.lcsc.com/product-detail/C149504.html) |
| R7 | UNI-ROYAL 0805W8F3300T5E 330ohm1% | 1 / 100 | $0.50 | Listed price; [source](https://www.lcsc.com/product-detail/C17630.html) |
| R10 | UNI-ROYAL 0805W8F1001T5E 1k1% | 1 / 100 | $0.35 | Listed price; [source](https://www.lcsc.com/product-detail/C17513.html) |
| J1 | JST B2B-PH-K-S(LF)(SN) vertical2mm | 1 / 20 | $0.71 | Listed price; [source](https://www.lcsc.com/product-detail/C131337.html) |
| U1 sockets | 2.54mm1x7 straight female socket strip | 2 / 2 | $1.00 | Budget estimate; not verified checkout quote; [source](https://www.pololu.com/product/1017) |
| U1 headers | 2.54mm1x7 male header | 2 / 2 | $0.20 | Budget estimate; allowance |
| BAT1 | SparkFun PRT-26059 protected1S1500mAh | 1 / 1 | $15.95 | Listed price; [source](https://www.sparkfun.com/lithium-ion-battery-1500mah-iec62133-certified.html) |
| Battery leads | Flexible insulated26–28AWG copper wire; short red/black pair | 1 / 1 | $1.00 | Budget allowance for usable wire; full spool extra; allowance |
| PCB | 84x78mm2layer1.6mmFR4 bare PCB | 1 / 5 | $2.00 | Unquoted introductory-price estimate; allow$2–5 batch; [source](https://jlcpcb.com/) |
| Case | Base+cover printedPLA/PETG | 1 / 1 | $1.50 | Material estimate; machine/service fees excluded; allowance |

## Choices and critique

The $55–75 planning range assumes consolidating purchases into two or three shipments, with tools and printer access already available. The source links identify parts; they are not instructions to place six separate store orders. Buying separately from every linked store can exceed that allowance. Buy compatible generic sockets/headers with the small-component order, and combine the controller, inductor and battery with one domestic supplier where available. Recheck its stock and prices before checkout. There is no final shipping, tax or tariff quote.

The XIAO already provides the charger; buying a TP4056 adds cost and is unnecessary. The RGB boost converter and I/O expander are needed for this selected controller/layout, so the new purchases are more than just a battery. The reference battery is chosen for its documented1.5A discharge rating and case footprint. Cheaper unbranded cells with only a capacity label are not equivalent.

[Adafruit2581200mAh](https://www.adafruit.com/product/258) is$9.95, saving$6 at the item price, but measures62x34x5mm and is rated1.2A continuous by its linked datasheet. It needs changed battery guides and a rechecked power budget; it is excluded from the primary total.

Gemini Argon reviewed the topology and BOM in multiple exchanges. Accepted points: account for minimum orders, check recoverable LED quantity, test desoldered encoders/LEDs, include wire/socket costs and a realistic soldering process. The original slide switch full-load current issue is corrected byQ1/Q2+R9/R10. Gemini initially invented several specifications and later retracted them; the audit report distinguishes manufacturer evidence from model opinion.

Keep twelve usable LEDs in the inventory. If salvage fails, buy fresh exactSK6812MINI-E spares; **their replacement price and shipping are not quoted in this total**. Two encoder knobs may be reused if owned; otherwise print or buy after measuring the shafts. Optional rubber feet, USB-C data cable, solder, flux, paste, tweezers, heat-set installation tool and hot-air/reflow access are not confirmed owned. They are excluded from the subtotal; allow$3–8 for small consumables/knobs/feet if needed, and obtain a separate quote for tools or assembly services.

The tinyTPS61023 SOT563 is1.6x1.2mm. A successful through-hole Hackpad build does not prove that this assembly process is available. Borrowing suitable equipment can be cheaper than buying it.

## Before ordering

Confirm actual battery/header dimensions and polarity, print an insert-hole coupon, count/test reusable parts, verify selected capacitor DC-bias data, and finish firmware/current measurements. The motherboard has not been manufactured or bench-tested. Budget25% RGB brightness initially; do not assume full white fits a500mA USB source. Charging is intentionally disabled when the battery switch isOFF.

No OLED is included; the lost display and the oldRP2040 are not purchases for this design.
