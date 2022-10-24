# A3 Use Case


## 3A: Goal of the tool

1. Goal of the tool  
To provide early LCA estimations for the buildings envelope of projects with IFC models.

2. Model use  
The use case is Sustainability and the BIM use is within the category Analyse - Forecast. Our use case is the ability to use LCA to predict future impacts of the environment. Making the user able to make proactive solutions regarding the building envelope before the build phase.

## 3B: Tool / Workflow

3. Process diagram  
<img src="../A1/Images/Preliminary BPMN.svg">

4. Description of workflow  
The proces starts with the user adjusting the BIM model to make it usable for LCA. This means materials is needed, as for example different insulation materials can have large varying impacts. BIM file is then exported into our tool as an IFC file. The tool will then do simplified quantities and material properties to give a simple LCA assessment. Furthermore energy framing is also calculated in a simple manor. Ideally the code could include EPD's for the used materials in the building.

## 3C: Information Exchange  

View the uploaded Excel file:
5. Information exchange  

6. IFC
We would need the IFC entities corresponding to the elements specified in the Excel file. For comparison of the results we would need requirements from BR18 to see whether the results are withing the limits of the requirements. The properties of the entites would have to contain materials of the specific entities and the amount of material for each entity. If materials for all entities can be extracted then we can easily make an overview of the environmental impacts using either provided EPDs or existing ones on corresponding materials.

## 3D: Value of tool

7. Business value  
The business value of our tool will be to save the company time when looking at different envelope/material solutions of a building in the early stages. As sustainability has become more important than ever in the building industry the simplification of the tool's output will also help employees with lesser knowledge on LCA understanding the solution space gain.

8. Societal value  
On a societal level the tool could help companies making better sustainable solutions by reducing material usage in the design phase.

## 3E: Delivery

9. Solving the use case

10. Making of the tool
