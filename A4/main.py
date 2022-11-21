import json
import ifcopenshell
import os
import time
import uuid

#IFC file import is taken from https://github.com/timmcginley/
'''
    load the IFC file
'''
name = "Duplex_A_20110907"

model_url = name+".ifc"
start_time = time.time()

if (os.path.exists(model_url)):
    model = ifcopenshell.open(model_url)
    print("\n\tFile    : {}.ifc".format(name))
    print("\tLoad    : {:.2f}s".format(float(time.time() - start_time)))

    start_time = time.time()
    print("\tConvert : {:.4f}s".format(float(time.time() - start_time)))

else:
    print("\nERROR: please check your model folder : " +model_url+" does not exist")


walls = model.by_type("IfcWallStandardCase")
materialLayers = model.by_type("IfcMaterialLayerSet")
area = 0
list = []
idnode = []
idedge = []
idconstructionedge = []

#Extracting material names and volumes from IfcWallStandardCase
for entity in walls:
    for relDefinesByProperties in entity.IsDefinedBy:
         for prop in relDefinesByProperties.RelatingPropertyDefinition.HasProperties:
             if prop.Name == 'Reference':
                 wallName = prop.NominalValue.wrappedValue
                 #print("\n"+str(wallName))
             if prop.Name == 'Area':
                 wallArea = prop.NominalValue.wrappedValue
                 #print("Area: " + str(wallArea))
    for relAssociatesMaterial in entity.HasAssociations:
             for test in relAssociatesMaterial.RelatingMaterial.ForLayerSet.MaterialLayers:
                 materialName = test.Material.Name
                 materialThickness = test.LayerThickness
                 materialVolume = materialThickness*wallArea
                 #print(str(materialThickness) + " " + str(materialName))
                 #print("volume: " + str(materialVolume))
                 if materialName not in list:
                    list.append(materialName)
                    list.append(materialVolume)
                    idnode.append(str(uuid.uuid4()))
                    idedge.append(str(uuid.uuid4()))
                    idconstructionedge.append(str(uuid.uuid4()))
                    
                 else:
                    list[list.index(materialName)+1] += materialVolume

#Creating initial json file data
data = []
condata = [{
        "Node": {
            "Construction": {
                "id": "c6f24e0f-020a-4f0f-93c6-65beb50bd798",
                "name": {
                    "Danish": "IfcWallStandardCase"
                },
                "unit": "M2",
                "source": "User",
                "comment": "",
                "layer": 1,
                "locked": True
            }
        }
    }]



#Writes the json file for each material
#Unique IDs, Material name, material volumes
for i in range(int(len(list)/2)):
    data.append ({
        "Node": {
          "Product": {
            "id": idnode[i],
            "name": {
              "English": "Test product",
              "Danish": list[i*2],
              "German": ""
            },
            "source": "User",
            "comment": "",
            "uncertainty_factor": 1.0,
            "uncertainty_factor_dgnb": 1.0
          }
        }
      })
    data.append ({
        "Edge": [
          {
            "ProductToStage": {
              "id": idedge[i],
              "excluded_scenarios": [],
              "enabled": True
            }
          },
          idnode[i],
          "61a77bc8-bddb-4521-9862-e613e26a5661"
        ]
      })
    condata.append ({
        "Edge": [
          {
            "ConstructionToProduct": {
              "id": idconstructionedge[i],
              "amount": list[i*2+1],
              "unit": "M3",
              "lifespan": 100,
              "demolition": False,
              "delayed_start": 0,
              "enabled": True,
              "excluded_scenarios": []
            }
          },
          "c6f24e0f-020a-4f0f-93c6-65beb50bd798",
          idnode[i]
        ]
      })

#Change directory to the LCAbyg import folder
os.chdir(r'C:\Program Files\SBi\LCAbyg 5 (64 bit) (5.2.1.0)\import_example')
# Create new JSON file with the new data
with open("products.json","w") as f:
    json.dump(data, f, indent=2)

with open("constructions.json","w") as f:
    json.dump(condata, f, indent=2)

#Close the file    
f.close()
