"""Conservative clearance geometry in U1 footprint-local coordinates.

Sullins LFB female housing: 8.50 mm high, 2.54 mm wide, 18.28 mm
long for seven positions. The 2.54 mm male-header plastic height is
an explicit assembly assumption, not a verified Seeed mating dimension.
Contacts and cosmetic details are omitted. Native KiCad adds the carrier
top datum and footprint rotation when exporting this model.
"""
import pathlib
import cadquery as cq

solids=[]
for y in [-7.62,7.62]:
    solids.append(cq.Workplane('XY').box(18.28,2.54,8.50).translate((0,y,4.25)).val())
    solids.append(cq.Workplane('XY').box(18.28,2.54,2.54).translate((0,y,9.77)).val())
model=cq.Compound.makeCompound(solids)
assert model.isValid()
cq.exporters.export(model,str(pathlib.Path(__file__).with_suffix('.step')))
