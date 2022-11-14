# A4: Final Project

## The tool
The tool will help automatically fill in volumes in LCAByg 5.2.1.0 from an ifc model with the necessary data. The python identifies the walls and from here extracts the materials and the volumes of materials used for the walls. After this it identifies the file called products.json in the json template files in this repository and takes the name and index of the product.

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
       -
               name: {Danish: "Project template"}
               res: 
                     - JsonFolder: C:\Program Files\SBi\LCAbyg 5 (64 bit) (5.2.1.0)\import_example
                     - Embedded: b5ca0ecf-52fc-461c-babe-7c763dc067ef
            



In this assignment we will develop a tool / workflow based on the use case you defined in the previous assignment.
The tool must:

Address your use case:
Ideally be written in Python, but can be other approaches in special cases if agreed with the course responsible.
Be summarised in a 2 minute video. You will produce one final tool in the following folders, the structure of which is summarised below.

## Tool / Workflow
The structure of this depends on the tool you have chosen to develop but it should:

1. be written in Python (mostly) so should contain a main.py file
2. if you have used blender as the target for the tool, please also include a .blend file that we can load to check your project.
3. clearly seperated the code from the input data and resulting guidance (output) (if your output is a file).


## 2 Minute Video
- Summary of the use case / why is this a challenge?
- Who is your tool for?
- Business and societal value
- Demo of the tool (if interaction / processing takes longer – edit the video 😊)



