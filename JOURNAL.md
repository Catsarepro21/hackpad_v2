---
title: "Hackpad"
github: "https://github.com/Catsarepro21/hackpad_v2"
description: "A(nother) custom hackpad! I made one before for Keeb but it was really bad because I wasn't that good at PCB's, so i'm making a much better one, and I even have some parts left over."
created_at: "2026-10-15"
total_time: "6h 42m"
---

# October 15, 2026: Schematic, PCB, code, and case, so pretty much everything
<!-- fabricate:entry 503 -->

So I first wanted a much better layout, so I started by drawing in excalidraw.

![](https://fabricate.hackclub-assets.com/3065f89b1a5546d5211209015aaef6c01872c941d393926718ac7158c1bf26ce/image-png/image.png)
. 
Then I started on the schematic, and I wanted bluetooth on this hackpad rather than not, and chose to add RGB under every key and around the edges. Then I made the schematic using an ESP32-S3(Kinda overkill but good for making it simpler), added all the RGB, rotary encoders, i removed the OLED cuz i lost it, and made sure to have a switch and battery connecter, and added 3d models for the parts from grabcad, just for reference to make sure it looked good and assigned all the footprints based on the known parts that I already have.

![](https://fabricate.hackclub-assets.com/8b15c6e68f56a8855f5abd3e4a8b67d18dc143e6ba2c48af3194f334c90754b6/image-png/image.png)

Then i made the PCB, and I just used normal 19.05 mx spacing and layed it out pretty quickly. I just dragged out the footprints in the grid for the keys and encoder, and I did the same for the ESP32, other parts i layed out where there was space to keep it square and I added RGB right under every key. And of course, i added M3 mounting holes so it would actually stay in my case.

![](https://fabricate.hackclub-assets.com/f93be0d5084b9e2b5477d5ade700596049fad41872df79c2c9a04fa5e2506a7b/image-png/image.png)

After that i made the case in onshape, I imported the PCB and just added a margin, made a sketch based on the PCB and mounting holes, and extruded to make the bottom half. Then I used ai03 Plate Generator to generate the top half DXF and extended it and extruded the mounting holes through it, and added a hole for the switch.


![](https://fabricate.hackclub-assets.com/c060103f218c86345a3f135842172f8d63e07f285e3cbcb29c341343b4de21d8/image-png/image.png)
Finally I made really basic code pretty quickly using Arduino IDE, and i did use Gemini's help a bit on this part but i did write it myself.

**Total time spent: 4h 30m**

# October 17, 2026: Cheapified
<!-- fabricate:entry 619 -->

I simplified the hackpad to bring the estimated parts order down to **$34.07 before tax**:

- Connected the keys and encoder clicks directly to the XIAO, so I don’t need to populate the MCP23008 or its supporting parts.
- Made RGB USB-only, letting me leave the battery RGB boost converter and its supporting parts unpopulated.
- Kept those extra footprints on the PCB so I can add the features later.
- Switched to a smaller protected 500mAh battery and used the XIAO’s built-in charger.
- Reused my existing switches, keycaps, encoders, LEDs, diodes, screws, and inserts.
- Consolidated the new parts into one DigiKey order.

![](https://fabricate.hackclub-assets.com/ea7b262b9ecc8e9b3bc75cfbf06daba572af6878d270d3e00efcf92fac2a871f/image-png/image.png)

**Total time spent: 1h 30m**

# October 20, 2026: Simplified Schematic and updated README and expanded Journal
<!-- fabricate:entry 772 -->

So today all i did was simplify the schematic by copying and pasting everything onto one page and removing the net labels and replacing with wires. Then I rewrote my readme and expanded my previous journals.

![](https://fabricate.hackclub-assets.com/9425fe2c5f5892aa9ce708a875369f32c8be9bd708c5da58b0de838f6bc1f392/image-png/image.png)

**Total time spent: 42m**
