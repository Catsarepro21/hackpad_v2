# Release audit - 18 October 2026

Status: electrical CAD checks pass; complete assembly is not production-qualified.

## PCB and schematic

KiCad checks report zero ERC violations, zero DRC violations, zero unconnected items and zero schematic parity issues. Existing LED aperture and fine-pitch converter clearance rules are retained; general clearances were not relaxed. All 221 netlisted pin assignments match the PCB, and schematic/PCB DNP sets match. The mechanical correction changes 3D-model transforms; copper, pads, holes, nets, footprint positions/rotations and fabrication geometry remain unchanged. Fresh Gerber/drill exports reproduce the published manufacturing package after removing creation-date metadata. All optional upgrade pads remain. A separate scratch project also enables formerly ignored check categories: zero ERC/DRC violations, zero unrouted items/parity issues, and no ignored categories in the resulting reports.

## STEP and case corrections

The PCB STEP is regenerated from the current native PCB, including DNP component models. Broken model references were removed or replaced, and model origins were aligned to the footprint geometry. Both encoder models use the same PCB seating datum. SW7 uses a conservative C&K JS102011SAQN clearance envelope, including both actuator positions, rather than a vendor cosmetic model. Its 9 x 3.6 x 3.5 mm body and 2 mm actuator travel follow the manufacturer drawing. The switch opening retains 0.4 mm nominal clearance at its inner edge.

The plate was formerly 1.6 mm too low. Its corrected z range is 5.1â€“6.6 mm above PCB bottom, with 1.5 mm thickness and 3.5 mm spacers above the nominal 1.6 mm PCB. The 90 x 84 mm XY outline and mounting locations are preserved; the total case height increases from 23.4 to 25.0 mm. Battery-pad wire access uses a 4.4 x 7.5 mm slot spanning both BAT+ and BATâˆ’ attachment holes. Complete and exploded assemblies use the corrected geometry. The regenerated case/interference reports record nominal-model validity, intersections and battery clearances; board parity compares the exported board core with the native PCB.

The corrected XIAO placement represents a nominal 11.04 mm gap from carrier-board top to module PCB underside: the verified 8.50 mm Sullins socket housing plus an assumed 2.54 mm male-header plastic height. The supplied native module model is positioned to that nominal gap. This is a clearance assumption, not a qualified exact mated-header model. Confirm the purchased male-header height, seating and USB plug/cable access in the first assembly.

## Release holds

The corrected plate/model arrangement substantially reduces the former MX overlaps. The approximate switch models still show two small plate intersections at each switch, about 0.328599 + 0.00117349 = 0.329773 cubic mm per switch. Some features resemble snap retention, but that does not establish intentional engagement for the exact owned switch. The 14.05 mm apertures were not enlarged blindly, which could weaken retention. Test an actual owned switch in a printed plate sample before a final case batch. The earlier 1.846 cubic mm overlap figure describes the superseded geometry.

Repository firmware is unchanged and incompatible with the simple direct matrix: it still scans the DNP MCP23008 and assigns GPIO1/5/6 to their old RGB-enable/I2C roles. The build instructions provide the required direct-matrix pin map. A separately supplied compiled candidate is not the repository firmware and has not established USB/BLE HID behavior on this hardware. Battery charging/disconnect, USB RGB current, actual battery connector polarity, cable access, antenna placement, owned encoder dimensions and printed tolerances require first-article verification. CAD and rule checks do not demonstrate these behaviors.

## BOM and price scope

All 78 PCB references are covered exactly once: 25 purchased components, 28 owned components, 14 DNP, seven solder jumpers and four mounting holes. Both shopping CSV copies and the Markdown shopping table agree. The rebuilt October 17 cart, Web ID 378054863, contains the 14 shopping lines, including ten R8/R9 resistors for $0.36; two are installed and eight are spares. This supersedes the older cart's inconsistent resistor quantity field.

The saved estimate is $23.57 parts + $8.49 estimated ground shipping + $2.01 estimated tariffs = $34.07 before tax. It was not refreshed at checkout on October 18. PCB fabrication, its delivery, printing and consumables are extra. No order has been placed.

[Shared rebuilt cart](https://www.digikey.com/short/m3zh375z) Â· [C&K JS series drawing, page I-54](https://www.tti.com/content/dam/tti-commons/supplier/c-k-components/doc/ck-js-series-sub-miniature-slide-switches-datasheet-specifications.pdf) Â· [Sullins socket drawing](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/937/Female_Headers.100_DS.pdf)

[Detailed CAD corrections and model limits](CAD-correction-report.md) · [Socket bounds](Socket-clearance-check.json) · [Native model-only comparison](Native-model-only-check.json) · [Print-mesh checks](STL-check.json)
