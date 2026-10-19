# CAD correction and verification - October 18, 2026

The enclosure's MX mounting plane used the board-bottom datum. Cherry specifies approximately 5.0 mm between PCB top and plate top. With the 1.6 mm PCB, the corrected plate is z=5.1 to 6.6 mm. The base walls and plate spacers rise 1.6 mm to meet it; outer size becomes 90 x 84 x 25 mm. The 14.05 mm square apertures, switch centers, PCB mounting points, floor, battery clearance and PCB remain unchanged. All plate cutters were extended to remain through-holes.

The BAT-pad opening now covers both BAT+ and BAT-: a 4.4 x 7.5 mm rounded slot centered at (102.43,-85.35), radius 2.0 mm. It leaves a nominal 1.27 mm web to the encoder aperture. ENC1's accidental extra 0.5 mm model lift was removed to match ENC2's identical footprint/model.

## Verification

- Native PCB comparison excludes only 3D model entries: every other S-expression is identical. Pads, footprint placements, nets, routing, zones, drills and settings are unchanged.
- Final PCB STEP is the native KiCad export, not a reconstructed board. The independent expected-transform comparison matched all 228 solid bounding boxes before the final identical-part encoder-height correction. The final STEP is copied byte-for-byte into the case's input and all complete/exploded case assemblies are regenerated from it.
- Base and plate are valid single solids. Their mutual overlap, battery-envelope overlap and reserved battery-volume/PCB overlap are all zero.
- Final STL base and plate are closed edge manifolds with consistent winding, and their print orientation starts at z=0. Plate STL includes its integral spacers.
- Full-population native STEP has zero base collisions. The only plate collisions are the imperfect supplied MX models: approximately 0.329773 cubic mm per switch after corrected model registration, compared with approximately 1.84559 before. This remains an explicit limitation, not a clean fit result.
- Socket envelopes and raised XIAO have zero case overlap. Module underside gaps of 8.5, 10.5, 11.04 and 12.0 mm were tested. A 16 x 24 x 9 mm assumed USB plug/cable corridor clears the case at the lowest stack height, with 1.355 mm vertical clearance above the plate. A particular purchased cable is not qualified by that envelope.
- SW7's complete actuator-travel clearance envelope has zero case overlap. The side opening retains 0.4 mm nominal inward clearance around its body and 2.0 mm at its ends. The actuator is recessed about 2.2 mm from the outer wall; finger/owned-switch access still needs physical checking.

## Model limits and assembly check

The two Sullins female housings are drawn from the manufacturer's 8.50 mm housing height, 2.54 mm width and 18.28 mm length. The male-header plastic is an explicit assumed 2.54 mm clearance envelope, not an exact Seeed mated-stack drawing. The nominal carrier-top-to-module-PCB-underside gap is 11.04 mm; the module underside is z=12.635 mm and USB shell z=12.895 to 17.095 mm. Because the source module model began 0.25 mm below the carrier top, its native model offset is raised 11.29 mm to produce that gap. Its 14 header-hole axes are aligned with the footprint.

MX model XY registration follows the central peg axis; its flange underside is aligned with the corrected plate top. The keycap socket center was measured in horizontal sections and aligned independently. These supplied models are approximate: side locating pegs are 10.00 mm apart while the correct PCB footprint is 10.16 mm. After centering, each 1.60 mm model peg is 0.08 mm off a 1.70 mm hole axis, leaving about 0.03 mm nominal radial interference. The model's large housing-bottom plane also sits about 0.30 mm above the PCB; modeled pin/central-peg tips are z=-1.30/-1.40 mm. Thus the model cannot prove real switch seating. Do not alter PCB holes or widen all plate holes to hide these model defects.

An optional small fit coupon is supplied to test the actual owned switch and print process. The final plate retains 14.05 mm apertures. Its 14.15 and 14.25 mm coupon alternatives are experiments for printer/owned-part fit, not changes to the final enclosure. Verify clip seating, retention, travel, wobble and solder-pin reach on the actual parts.

The local XIAO footprint now retains its two corrected model entries. The six MX footprints use the standard KiCad library; retain custom 3D models when updating those footprints from the library. Exact owned encoder/knob dimensions, flexible battery leads, antenna placement, physical print tolerances and first-article operation remain outside this CAD proof.

## Drawing sources

- [Cherry-authored MX Series drawing, pages 10-3 and 10-4](https://raw.githubusercontent.com/keyboardio/keyswitch_documentation/master/datasheets/Cherry/mx_series.pdf): 0.197 +/- 0.012 inch PCB-top-to-plate-top spacing; 0.551 +/- 0.002 inch aperture; 0.060 +/- 0.004 inch plate thickness.
- [Sullins female-header drawing](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/937/Female_Headers.100_DS.pdf): LFB housing 8.50 mm high, 2.54 mm wide; seven-way body 18.28 mm long.
- [Seeed 102010490 header](https://www.seeedstudio.com/XIAO-Series-7-Pin-Male-Header-5-pcs-p-5460.html): exact purchased part identification; the assumed plastic height above is not presented as a verified mating drawing.
