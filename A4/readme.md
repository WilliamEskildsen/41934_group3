# A4: Final Project

## Aim and scope of the tool

The scope of the study is limited to IFCWallStandardCase (walls within the ifc model). The other ifc components follow the same principles, but due to time limit the scope has been set to IFCWallStandarCase.

- [x] Extracting material name and volume from ifc 
- [x] Writing material name and volume to json file
- [x] Importing json file to LCAByg
- [ ] Saving epd's to materials from LCAByg

## The tool
This tool uses open source licensing. The tool will help automatically fill in volumes in LCAByg 5.2.1.0 from an ifc model with the necessary data. The python script identifies the walls and from here extracts the materials and the volumes of materials used for the walls. After this it writes a file called products.json and construction.json as the json template files in this repository with the names and indexes of the products (example of json file seen in code below). 


        {
                "Node": {
                    "Product": {
                        "id": "51bcec85-9105-4946-8a8a-51219bf9adfa",
                        "name": {
                            "Danish": "Test byggevare",
                            "English": "Test product",
                            "German": ""
                        },
                        "source": "User",
                        "comment": "",
                        "locked": true
                    }
                }
            }


        {
                "Edge": [
                    {
                        "ConstructionToProduct": {
                            "id": "65cc0492-7864-4598-9254-5f929379bae6",
                            "amount": 1,
                            "unit": "M2",
                            "lifespan": 100,
                            "demolition": false,
                            "enabled": true,
                            "delayed_start": 0
                        }
                    },
                    "c6f24e0f-020a-4f0f-93c6-65beb50bd798",
                    "51bcec85-9105-4946-8a8a-51219bf9adfa"
                ]
            }

After the python script creates the json files, the folder import_example can be loaded in to LCAByg and it will have the materials from the components read from the ifc file.

## Requirements to run tool

To run the tool you will need the following softwares and files downloaded from this 

### Softwares
1. LCAByg 5.2.1.0 (No other versions)
2. IDLE 3.1 (To run the python script with appropriate libraries)
3. IFCOpenshell 

### Files needed
1. main.py (from this repository)
2. duplex.ifc (from this repository)
3. The folder called import_example from this repository

### Stepwise guide
1. Take import_example and paste it under C:\Program Files\SBi\LCAbyg 5 (64 bit) (5.2.1.0)
2. In the above folder open engine.yaml as administrator (can be done with notepad++)
3. Add the following under the existing lines of code

       -
               name: {Danish: "Project template"}
               res: 
                     - JsonFolder: C:\Program Files\SBi\LCAbyg 5 (64 bit) (5.2.1.0)\import_example
                     - Embedded: b5ca0ecf-52fc-461c-babe-7c763dc067ef
4. Now you can run the main.py code in IDLE (duplex.ifc has to be in the same folder as main.py and you will need to have the module ifcopenshell to be able to import it using main.py)


## Further work
To expand the tool further we want to make it more automatic to link all products to specific building parts and link epds from the LCAByg database to the fitting materials based on material names from ifc. Furthermore it would be the goal to strive for, that the tool may be able to build all the relating categories under LCAByg so that you would automatically have a full LCAByg file and not just material volumes. This can be done so that the tool works with speckle and can update and make quick overlays of impacts on the climate based on materials and volumes used in a building project. To make the societal value bigger it would be nice if the tool could take the results from LCAByg and upload them to a webpage explained so that all people (no need for engineering background) can understand the results.


## 2 Minute Video
- Summary of the use case / why is this a challenge?
- Who is your tool for?
- Business and societal value
- Demo of the tool (if interaction / processing takes longer – edit the video 😊)




