# Release audit - 17 October 2026

Status: electrical CAD checks pass; complete assembly is not production-qualified.

## PCB and schematic

Final KiCad checks report zero ERC violations, zero DRC violations, zero unconnected items and zero schematic parity issues, with existing project exclusions retained. The PCB source is identical to the previous checked version after removing 3D-model entries: copper, pads, holes, component placements and fabrication data are unchanged. The Gerber/drill ZIP therefore remains applicable. All optional upgrade pads remain.

## STEP and case corrections

The PCB STEP was regenerated directly from the current native PCB, including DNP component models. Nine broken model references were removed or replaced while retaining the valid local encoder and MX models. SW7 previously had no usable model. Its replacement is a conservative C&K JS102011SAQN clearance envelope, including both actuator positions, not a vendor cosmetic model. Its 9 x 3.6 x 3.5 mm body and 2 mm actuator travel follow the manufacturer drawing. The switch cover opening was widened inward by 1.2 mm, preserving the case exterior and mounting locations. The previous cover overlapped the switch body by 0.8 mm (10.8 cubic mm); the corrected opening provides 0.4 mm nominal clearance at that edge.

The regenerated complete and exploded assemblies include this switch envelope. The battery envelope and reserve, case validity, tray/plate separation, and PCB-to-case checks are recorded in the JSON reports.

## Release holds

The supplied MX models overlap the 14.05 mm square plate apertures slightly at all six switches: approximately 1.846 cubic mm per switch, with side intrusions up to 0.1294 mm and low clip-tip intrusions to about 0.2299 mm. Some overlap is consistent with snap clips, but the model also has a small center offset relative to the nominal aperture. No claim that all overlap is intentional has been established. The aperture was not enlarged blindly because that could weaken switch retention. Check the actual owned switches in a plate sample before a final case batch.

Firmware is unchanged and still needs conversion from the MCP23008 scanner to the direct matrix pin map. USB/BLE HID, battery charging/disconnect, USB RGB current, actual battery connector polarity, cable access, antenna placement and printed tolerances require first-article verification. These are not demonstrated by CAD or rule checks. Fabrication-ready electrical files do not establish a tested production assembly.

[C&K JS series manufacturer drawing, page I-54](https://www.tti.com/content/dam/tti-commons/supplier/c-k-components/doc/ck-js-series-sub-miniature-slide-switches-datasheet-specifications.pdf)
