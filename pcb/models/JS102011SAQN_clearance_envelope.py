import sys,pathlib
# Requires CadQuery 2.8 or compatible installation.
import cadquery as cq
out=pathlib.Path(__file__).resolve().parent;out.mkdir(exist_ok=True)
body=cq.Workplane('XY').box(9,3.6,3.5,centered=(True,True,False))
# Conservative swept actuator envelope: includes both 2mm-apart detents.
body=body.union(cq.Workplane('XY').box(3.5,2,3.5,centered=(True,True,False)).translate((0,-2.8,0)))
for x in [-2.5,0,2.5]:body=body.union(cq.Workplane('XY').box(.6,2,.3,centered=(True,True,False)).translate((x,2.75,0)))
for x in [-3.4,3.4]:body=body.union(cq.Workplane('XY').center(x,0).circle(.4).extrude(-.8))
assert body.val().isValid()
cq.exporters.export(body,str(out/'JS102011SAQN_clearance_envelope.step'))
