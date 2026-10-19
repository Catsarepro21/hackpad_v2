import sys,pathlib,json
import cadquery as cq
from OCP.Bnd import Bnd_Box
from OCP.BRepBndLib import BRepBndLib
out=pathlib.Path(__file__).resolve().parent
def bb(s):
 b=Bnd_Box();BRepBndLib.Add_s(s.wrapped,b,False);return b.Get()
def box(x,y,z,dx,dy,dz):return cq.Workplane('XY').box(dx,dy,dz).translate((x,y,z))
def roundbox(x,y,z,dx,dy,dz,r):return box(x,y,z,dx,dy,dz).edges('|Z').fillet(r)
# Coordinates match the KiCad STEP: PCB bottom z=0, top z=1.6.
# 0.4 mm board clearance, 2.6 mm walls, 2.4 mm floor, 16 mm under-board space.
cx,cy=90,-105
base=roundbox(cx,cy,(-18.4+5.1)/2,90,84,23.5,6)
inner=roundbox(cx,cy,(-16+15)/2,84.8,78.8,31,3.4)
base=base.cut(inner)
mounts=[(55,-73),(127,-73),(55,-139),(127,-139)]
for x,y in mounts:
 boss=cq.Workplane('XY').center(x,y).circle(4).extrude(16).translate((0,0,-16))
 base=base.union(boss)
 # M3 screw clearance and blind top-loading heat-set insert pocket.
 base=base.cut(cq.Workplane('XY').center(x,y).circle(1.7).extrude(17).translate((0,0,-16)))
 base=base.cut(cq.Workplane('XY').center(x,y).circle(2.3).extrude(4.4).translate((0,0,-4.4)))
# USB cable access at the rear/top edge, switch access on the right.
base=base.cut(box(91,-64,5,16,8,11))
base=base.cut(box(132.4,-130,3,11.2,13,9))
# Battery guides provide 40.2 mm width for the Adafruit 1578 clearance envelope.
for x in [70,112]:base=base.union(box(x,-117,-15,1.8,33,2))
# Cherry MX plate top is 5.0 mm above PCB top (absolute z=6.6 mm).
# Plate thickness follows MX switch clips; tall encoder housings pass through square apertures.
plate=roundbox(cx,cy,5.85,90,84,1.5,6)
for x in [72,91.05,110.1]:
 for y in [-102,-121.05]:plate=plate.cut(box(x,y,5.85,14.05,14.05,4))
for x in [70,113.5]:plate=plate.cut(roundbox(x,-80,5.85,15.2,15.2,4,.6))
plate=plate.cut(roundbox(91,-79,5.85,22.4,25,4,1))
plate=plate.cut(box(91,-64.5,5.85,16,8,4))
# Battery connector access and battery-pad wire clearance.
# J1 battery connector mounts inside below PCB; cover remains closed here.
plate=plate.cut(roundbox(102.43,-85.35,5.85,4.4,7.5,4,2.0))
plate=plate.cut(box(132.4,-130,5.85,11.2,13,4))
# Integral upper spacers stop the mounting screws crushing the 3.5 mm cover gap.
for x,y in mounts:
 spacer=cq.Workplane('XY').center(x,y).circle(3.5).extrude(3.5).translate((0,0,1.6))
 plate=plate.union(spacer)
 plate=plate.cut(cq.Workplane('XY').center(x,y).circle(1.7).extrude(7).translate((0,0,1)))
for x,y in [(70,-90),(113.5,-90),(54.5,-81),(127.5,-97),(78,-139.5),(105,-139.5)]:
 plate=plate.cut(cq.Workplane('XY').center(x,y).circle(2.2).extrude(6).translate((0,0,2)))
print('Case bodies built',flush=True)
for label,obj in [('Base_tray',base),('MX_switch_plate',plate)]:
 assert len(obj.solids().vals())==1 and obj.val().isValid(),label
 cq.exporters.export(obj,str(out/(label+'.step')))
 # Put STL on the build plane. The tray floor and plate flat face print down.
 print_obj=obj
 if label=='MX_switch_plate': print_obj=print_obj.rotate((0,0,0),(1,0,0),180)
 zmin=bb(print_obj.val())[2];print_obj=print_obj.translate((-cx,cy if label=='MX_switch_plate' else -cy,-zmin))
 cq.exporters.export(print_obj,str(out/(label+'.stl')),tolerance=.05,angularTolerance=.15)
ref=cq.importers.importStep(str(out.parent/'pcb'/'Fabricate_Wireless_Macropad.step'))
# Keep the PCB/components as a single reference body group to avoid the source STEP's nested imports.
pcb=cq.Assembly(name='PCB_reference')
for i,solid in enumerate(ref.solids().vals()):
 x1,y1,z1,x2,y2,z2=bb(solid)
 color=cq.Color(.5,.53,.56)
 name='Component_'+str(i)
 if x2-x1>80 and y2-y1>70:color=cq.Color(.15,.40,.27);name='PCB_84x78mm'
 elif z1>9 and x2-x1>16:color=cq.Color(.93,.92,.88);name='Keycap_'+str(i)
 elif z1>1.4 and z2<6.7 and x2-x1>12 and y2-y1>12:color=cq.Color(.13,.14,.16)
 elif z2<1.6:color=cq.Color(.25,.27,.29)
 pcb.add(solid,name=name,color=color)

case=cq.Assembly(name='Hackpad_V2_case')
case.add(base,name='Base_tray',color=cq.Color(.13,.17,.22))
case.add(plate,name='MX_switch_plate',color=cq.Color(.75,.81,.86))
case.export(str(out/'Hackpad_V2_case.step'))
assy=cq.Assembly(name='Hackpad_V2_complete')
assy.add(base,name='Base_tray',color=cq.Color(.13,.17,.22))
assy.add(plate,name='MX_switch_plate',color=cq.Color(.75,.81,.86))
assy.add(pcb,name='PCB_reference')
assy.export(str(out/'Hackpad_V2_complete.step'))
# Exploded presentation: plate lifted above the PCB, base lowered below it.
expl=cq.Assembly(name='Hackpad_V2_exploded')
expl.add(base.translate((0,0,-13)),name='Base_tray',color=cq.Color(.13,.17,.22))
expl.add(plate.translate((0,0,30)),name='MX_switch_plate',color=cq.Color(.75,.81,.86))
expl.add(pcb,name='PCB_reference')
expl.export(str(out/'Hackpad_V2_exploded.step'))
report={'base_valid':base.val().isValid(),'plate_valid':plate.val().isValid(),'base_solids':len(base.solids().vals()),'plate_solids':len(plate.solids().vals()),'outer_mm':[90,84,25.0],'pcb_mm':[84,78,1.6],'plate_thickness_mm':1.5,'under_pcb_clearance_mm':16,'mount_holes_mm':mounts,'pcb_bottom_z_mm':0,'plate_bottom_z_mm':5.1,'plate_top_z_mm':6.6,'battery_reserve_mm':[40,33,7],'battery_center_mm':[91,-117,-12.5],'integral_plate_spacers_mm':3.5,'base_plate_overlap_mm3':base.val().intersect(plate.val()).Volume()}
json.dump(report,open(out/'Enclosure-checks.json','w'),indent=2)
print(json.dumps(report),flush=True)





battery=box(91,-117,-12.5,36,29,4.75)
reserve=box(91,-117,-12.5,40,33,7)
report['battery_mm']=[36,29,4.75]
report['battery_to_base_overlap_mm3']=battery.val().intersect(base.val()).Volume()
report['battery_to_plate_overlap_mm3']=battery.val().intersect(plate.val()).Volume()
report['reserve_to_pcb_overlap_mm3']=sum(reserve.val().intersect(s).Volume() for s in ref.solids().vals())
report['battery_fit_scope']='Rectangular manufacturer envelope; flexible leads, adhesive restraint and physical tolerances require assembly check.'
json.dump(report,open(out/'Enclosure-checks.json','w'),indent=2)
print(json.dumps(report),flush=True)
