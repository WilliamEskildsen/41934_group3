import ifcopenshell
import bpy
from blenderbim.bim.ifc import IfcStore
file = IfcStore.get_file()

QA = file.by_type("IfcQuantityArea")

for Q in QA:
     print("Area: ", Q.AreaValue)


TotalArea = 0
for Q in QA:
    TotalArea += Q.AreaValue
    
print(TotalArea)



windows = file.by_type("IfcWindow")
TotalWindowArea = 0
for window in windows:
    TotalWindowArea += window.OverallHeight*window.OverallWidth
    
print(TotalWindowArea)