# Simple build shopping list

DigiKey cart Web ID **378054863**, rebuilt and captured October 17, 2026: **$23.57 parts + $8.49 estimated ground shipping + $2.01 estimated tariffs = $34.07 before sales tax**. At that capture, all 14 lines showed Immediate availability; the cart also warns of an additional processing day. These are saved cart prices, not a refreshed checkout quote. No LCSC order is needed for this population. Do not purchase both old carts and this one.

A rough 7.25-7.5% tax allowance gives about $36.54-$36.63 if applied to the entire $34.07; actual taxable base, delivery address and checkout determine the final total. ZIP 27560 alone does not establish an exact tax quote. PCB fabrication, its delivery, case printing and consumables remain unquoted. No order placed.

| Reference/use | Part | Needed | Cart quantity | Line USD |
|---|---|---:|---:|---:|
| U1 | XIAO ESP32-S3 113991114, 1597-113991114-ND | 1 | 1 | 7.49 |
| J1 | B2B-PH-K-S, 455-1704-ND | 1 | 1 | 0.12 |
| U1 sockets | PPTC071LFBN-RC, S7005-ND | 2 | 2 | 1.16 |
| U1 male headers | Seeed 102010490 five-pack | 2 strips | 1 pack | 0.25 |
| U4 | SN74AHCT1G125DBVR, 296-4708-1-ND | 1 | 1 | 0.14 |
| R8,R9 | RC0805FR-07100KL, 311-100KCRCT-ND | 2 | 10 | 0.36 |
| R7 | RC0805FR-07330RL, 311-330CRCT-ND | 1 | 1 | 0.10 |
| R10 | RC0805FR-071KL, 311-1.00KCRCT-ND | 1 | 1 | 0.10 |
| Battery pad leads | Adafruit 1954 wire pack, 1528-1964-ND | 1 pair | 1 pack | 1.95 |
| Q1,Q2 | AO3401A, 785-1001-1-ND | 2 | 2 | 1.04 |
| C1,C6-C18 | CC0805KRX7R9BB104 100nF 50V X7R 0805, 311-1140-1-ND | 14 | 14 | 1.37 |
| C4 | CL32B226KOJNNNE 22uF 16V X7R 1210, 1276-1855-1-ND | 1 | 1 | 0.64 |
| SW7 | JS102011SAQN, 401-1999-1-ND | 1 | 1 | 0.90 |
| Battery | Adafruit 1578 protected 500mAh, 1528-1841-ND | 1 | 1 | 7.95 |

Use the PCB-mounted C&K SW7. The earlier remote SK12D07 switch plan is superseded. Verify JST polarity before connecting the battery. The 500mAh battery measures 29x36x4.75mm and is rated 500mA maximum continuous discharge; this build reserves battery power for the controller, not LEDs. It has less runtime than the earlier 1200mAh option. The XIAO provides charging; no separate charger is needed.

Owned: six MX switches, six DSA keycaps, eight 1N4148 diodes, two EC11 encoders with clicks, twelve SK6812 MINI-E LEDs, four M3x16 screws, four 5mm OD x 4mm heat-set inserts. Solder bridges cost no extra components. Salvaged parts have not been electrically qualified.

Optional later: U2 MCP23008-E/SO; R1/R2 4.7k; R3 10k; C2 100nF; U3 TPS61023DRLR; L1 SRP5030T-1R0M; D9/D10 B340A-13-F; C3 C1206C106K8RACTU 10uF; C5 CL32B226KOJNNNE 22uF; R4 732k; R5/R6 100k. All corresponding footprints remain on the PCB. See [build instructions](Build-options.md) before populating them.

[Shared rebuilt cart](https://www.digikey.com/short/m3zh375z) · [Battery specifications](https://www.adafruit.com/product/1578) · [Battery datasheet](https://cdn-shop.adafruit.com/product-files/1578/Datasheet.pdf)

## Assembly coverage

[BOM.csv](BOM.csv) contains the 14 priced shopping lines only. The tables below complete the PCB population list; owned and DNP parts do not add to the shopping subtotal. There are 78 PCB references: 53 populated components, 14 DNP components, 7 solder jumpers and 4 mounting holes.

| PCB references | Qty | Use now | Package / requirement |
|---|---:|---|---|
| SW1-SW6 | 6 | Owned MX switches | Soldered PCB-mount MX; actual plate fit still needs checking |
| ENC1,ENC2 | 2 | Owned EC11 encoders with clicks | Match the Alps EC11E switch footprint and shaft dimensions; owned exact model not documented |
| D1-D8 | 8 | Owned 1N4148 | Axial DO-35, 7.62 mm lead pitch; observe cathode markings |
| LED1-LED12 | 12 | Owned SK6812 MINI-E | 3.2 x 2.8 mm reverse-mount; observe pin 1 and PCB apertures |
| JP1-JP7 | 7 | Solder only | Configure exactly as in the build instructions; no purchased jumper parts |
| MH1-MH4 | 4 | Mounting holes | Four owned M3x16 screws and four owned 5 mm OD x 4 mm inserts |

Other assembly items: six owned DSA keycaps, one fabricated 84 x 78 mm two-layer 1.6 mm PCB, and the printed base/plate. USB-C data cable, solder, insulation and battery restraint are not priced or assumed owned. Use the antenna supplied with XIAO 113991114; its routing/placement still needs assembly verification.

## Optional footprint population - do not buy for the simple build

| References | Qty | Part/value | PCB package |
|---|---:|---|---|
| U2 | 1 | MCP23008-E/SO | Wide SOIC-18, 7.5 x 11.6 mm, 1.27 mm pitch |
| U3 | 1 | TPS61023DRLR | SOT-563 |
| L1 | 1 | SRP5030T-1R0M | Bourns SRP5030T |
| D9,D10 | 2 | B340A-13-F, SS34 equivalent specified by original BOM | SMA |
| R1,R2 | 2 | 4.7k | 0805 |
| R3 | 1 | 10k | 0805 |
| R4 | 1 | 732k, 1% | 0805 |
| R5,R6 | 2 | 100k, 1% | 0805 |
| C2 | 1 | 100nF | 0805 |
| C3 | 1 | C1206C106K8RACTU, 10uF 10V X7R | 1206 |
| C5 | 1 | CL32B226KOJNNNE, 22uF 16V X7R | 1210 |

## Assembly details and remaining checks

The two U1 sockets are 7-way, 2.54 mm pitch PPTC071LFBN-RC. The male-header pack is Seeed 102010490 (DigiKey 1597-102010490-ND), containing five 7-pin strips; two strips are needed. The manufacturer drawing gives 8.50 mm socket insulation height (the catalog rounds this to 8.51 mm). The corrected CAD represents a nominal 11.04 mm gap from carrier-board top to XIAO PCB underside: 8.50 mm socket housing plus an assumed 2.54 mm male-header plastic height. The male-header height and final seating have not been verified for the exact purchased strip. Confirm actual module height, secure mating and USB plug/cable clearance in the first assembly before printing a final case batch; the nominal envelope does not qualify the exact mated connector stack. Solder the two battery leads directly between XIAO BAT pads and the labeled carrier BAT+/BAT- pads; Adafruit 1954 supplies 20 wires, so cut and strip two suitable leads rather than relying on loose jumper contacts for battery power.

The battery is protected Adafruit 1578, with a JST-PH plug matching the 2 mm J1 connector family; measure connector polarity before connection. Switch ON to charge. RGB remains USB-only. Read the [release audit](../docs/Release-audit.md) before treating this as a tested production assembly; firmware/direct-matrix scanning, MX plate fit and powered operation remain unverified.

Source checks, October 17, 2026: [socket dimensions and pitch](https://www.digikey.com/en/products/detail/sullins-connector-solutions/PPTC071LFBN-RC/810146), [Seeed module specification and supplied antenna](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/6209/Seeed%20113991114.pdf), [wire pack contents](https://www.adafruit.com/product/1954), [protected battery dimensions](https://www.adafruit.com/product/1578). The rebuilt October 17 cart establishes the listed prices; current stock, shipping, tariffs and tax must be reconfirmed at checkout.

R8/R9 order quantity: two are installed; the rebuilt October 17 cart correctly orders ten for $0.36 (eight spares). The older cart's inconsistent quantity field is superseded. The saved $34.07 estimate is before tax and must be refreshed at checkout.
