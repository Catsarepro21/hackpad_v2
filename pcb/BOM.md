# Simple build shopping list

DigiKey cart Web ID **378036726**, checked October 16, 2026: **$23.57 parts + $8.49 estimated ground shipping + $2.01 estimated tariffs = $34.07 before sales tax**. All 14 lines showed Immediate availability; the cart also warns of an additional processing day. No LCSC order is needed for this population. Do not purchase both old carts and this one.

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

Optional later: U2 MCP23008-E/SO; R1/R2 4.7k; R3 10k; C2 100nF; U3 TPS61023DRLR; L1 SRP5030T-1R0M; D9/D10 B340A-13-F; C3 C1206C106K8RACTU 10uF; C5 CL32B226KOJNNNE 22uF; R4 732k; R5/R6 100k. All corresponding footprints remain on the PCB. See Build-options.md before populating them.

[Live cart](https://www.digikey.com/ordering/shoppingcart) · [Battery specifications](https://www.adafruit.com/product/1578) · [Battery datasheet](https://cdn-shop.adafruit.com/product-files/1578/Datasheet.pdf)
