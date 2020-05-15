# Assembly of Blocks with Errors

#### Procedure Overview

  1. Save [ErrorBlocks.SLDASM](https://github.com/NybergWISC/model_development_workflow/blob/master/ErrorBlocks.SLDASM) and convert to ACIS format or directly save and open [ErrorBlocks.SAT](https://github.com/NybergWISC/model_development_workflow/blob/master/ErrorBlocks.SAT).
  2. Fix mistakes within the model using ANSYS SpaceClaim.
  3. Import file into Trelis/Cubit and inspect model for any import issues.
  4. Create the graveyard volume and define implicit complement.
  5. Finish model in Cubit/Trelis.
     * Imprint and Merge volumes
     * Assign materials
     * Export the model to .h5m

Exporting the model to .h5m requires the DAGMC trelis plugin, which should be installed before starting the tutorial. Instructions are [here](https://svalinn.github.io/DAGMC/install/plugin.html).

#### Goals of Example

  * Execute the workflow with a model that has geometric issues to be resolved in SpaceClaim.
  * Work through important processes on an example that is easy to visualize and understand.
  * Provide a general understanding of what issues could arise on more complex models.

## Procedure

### In Initial CAD program

_Any CAD engine should work for this process as long as it can export to a format importable by SpaceClaim or Cubit/Trelis._


  1. Download the [ErrorBlocks.SLDASM](https://github.com/NybergWISC/model_development_workflow/blob/master/ErrorBlocks.SLDASM) file from this page and open in Solidworks.
  2. Export the assembly/part to ACIS format (.sat file extension)
     * ACIS format 22 is preferred (default for Solidworks)
     * Use save or export feature and select ACIS (.sat) format

![ErrorBlocksOverviewWide](https://github.com/NybergWISC/model_development_workflow/blob/master/PicturesSnapshots/ErrorBlocks/ErrorBlocksOverviewWide.JPG)

<details><summary> Notes </summary><p>
- The preferred format is ACIS (.sat). Note that multiple file types could be used, but there is anecdotal evidence that suggests .sat files work the best for this process. Otherwise formats such as STEP and STL are also able to be imported to Trelis/Cubit.
<br/>
- This step is unnecessary unless you want to explore the model in Solidworks or learn how to save file as .sat.
<br/>
- To skip this step download the ACIS file titled "ErrorBlocks.sat" and move onto ANSYS SpaceClaim section.
</p>
</details>

### In ANSYS SpaceClaim
_SpaceClaim is useful for cleaning models that have general issues such as small gaps, overlaps, edge contacts, and unnecessary geometric detail. More general SpaceClaim tutorials/support can be found_ [here](http://www.spaceclaim.com/en/Support/Tutorials/Essentials.aspx).
  1. Open ErrorBlocks.sat by going to __File -> Open__ and then sorting by .sat type files.
  2. Identify all general issues which exist within the model:

      * Visually:
        - Find one example of each general issue as described below. All four are relatively conspicuous and easy to find visually.
      * With SpaceClaim tools:
        - To identify gaps navigate from __Prepare -> Clearance -> Detect__. In this case to find the gap enter a maximum distance of `1cm` in the Find Options box. The gap will be highlighted in red.
        - To identify overlaps navigate from  __Prepare -> Interference -> Remove.__ There are technically two volumes of interference and both will be highlighted in red.
        - The __Imprint__ tool highlights any coincident edges or faces within the part and can make it easier to find edge contacts as well as overlaps. This tool can be found by going __Prepare -> Analysis -> Imprint__.
        - There are no built-in tools in SpaceClaim to generally identify unnecessary details.

  <details><p><summary>Descriptions of General Issues </summary>
  Gaps: when particles encounter gaps they may lose track of which volume they are in and be lost. In this model there is one obvious gap, but for real models gaps are only an issue when the gap is around 10^-6 units (cm). In many cases small gaps can also be fixed by the imprint/merge step in Trelis/Cubit This gap is made larger in this example so that it can be found visually as well as with the SpaceClaim tool.
  <br/><br/>
  Overlaps: when particles encounter overlaps between two volumes they may not be able to determine which volume they are in and be lost. There is one volume that is obviously overlapping with other volumes.
  <br/><br/>
  Edge contacts: there is a possibility that when two volumes are only in contact on a single edge it can cause an issue with surface definitions. There is one example of an edge contact in this model.
  <br/><br/>
  Unnecessary Detail: all details in the CAD model are included in the faceting process and in the final analysis. Fine geometric details can be computationally expensive. The physical threads included in this model are one example of an unnecessary detail. In other models, whether fine geometric detail is considered unnecessary or not depends on the desired level of detail in the simulation and the computational resources available.
  </p></details>
<br/>

  3. Fix the general issues with the tools available in SpaceClaim.


| __Type of Issue__  | __Overview__  | __Procedure to fix__  | __Picture Example__ |
|---|---|---|---|
| __Gaps:__  | To fix gaps oftentimes the best option is to use the "Pull" tool and fix any possible overlaps using the "Interference" tool.  |   __Find the "Select" tool -> select one of the two surfaces -> click "Pull" tool -> "Up To" option -> click any face of the other component that borders the gap.__ <br/></br>This will extend one of the two volumes to fill the gap. <br/></br> To make it easier to see the face you can hide one of the two components by unchecking the box under the "Structure" toolbar.| ![ClearanceTool](https://github.com/NybergWISC/model_development_workflow/blob/master/PicturesSnapshots/ErrorBlocks/ClearanceTool.JPG "ClearanceTool") |
| __Overlaps:__  | The "Interference" tool gives the option to subtract an interfering/overlapping region from one of the two bodies.  | __Find the "Interference" tool -> select "Subtract" option.__ <br/></br> SpaceClaim automatically selects the larger component as the one to subtract from. To switch to the other volume simply check the box labeled "Subtract from smaller body" located in Fix Options.  | ![InterferenceTool](https://github.com/NybergWISC/model_development_workflow/blob/master/PicturesSnapshots/ErrorBlocks/InterferenceTool.JPG "InterferenceTool") |
| __Edge contacts:__   | There are two main ways to resolve edge contacts: <br/></br> 1. The first is to create a wider edge so that there is a common surface <br/></br> 2. The second is to cut out the edge so that there is are no shared features between the two components. <br/></br> This is dependent on the nature of the model and the analysis.  | - Go to __design tab -> sketch section -> select the line option.__ <br/></br> - Use lines to create a rectangle that is coincident to the surface with the edge contact and whose top and bottom edges are parallel to the top and bottom faces of the volume with the edge (pictured on the right). <br/></br> - __Find the "Select" tool -> select the rectangle -> click "Pull".__ </br></br> 1. To create a gap __select "Cut" from the "Options-Pull" toolbar -> either drag the cut to the bottom of the component, use the "Up To" option and select the bottom face, or use the "Ruler" option and make the pull 100cm.__ <br/></br> 2. To create a wider edge __select "Add" -> either drag the cut to the bottom of the component, use the "Up To" option and select the bottom face, or use the "Ruler" option and make the pull 100cm.__ <br/></br> This method will create interference between the new volume and old which can be resolved using the "Interference" tool.  | ![RectangleEdgeContact](https://github.com/NybergWISC/model_development_workflow/blob/master/PicturesSnapshots/ErrorBlocks/RectangleEdgeContact2.JPG "RectangleEdgeContact") |
| __Unnecessary details:__   |  In this particular case the physical threads are an unnecessary detail as they will cause a significant amount of computational load, but have very little effect on the final results. Which details are important to keep and which to delete is dependent on the nature of the model and the analysis.    | - This step can be completed in any CAD program and is more of a general suggestion to be considered continuously during the design phase. <br/></br> - In SpaceClaim one can use a circular pull to flatten the threads in a similar way to fixing an edge contact. | ![ScrewedUpDetails](https://github.com/NybergWISC/model_development_workflow/blob/master/PicturesSnapshots/ErrorBlocks/DetailCloseUp.JPG "ScrewedUpDetails") |

<details><p><summary>Notes</summary>
- Most often in real models unnecessary details must be determined intuitively and visually while overlaps, edge contacts, and small gaps cannot be found visually.
<br/></br>
- For all of these edits one must work closely with the creator of the model/experiment to determine which complications are important to the end result and which are able to be changed.
</p></details>

### In Cubit/Trelis
_Cubit is a meshing pre-processing software with CAD capabilities and Trelis is the commercially available version. It is used in this workflow to assign materials to volumes and export the model to the DAGMC .h5m format. Trelis and Cubit have both a GUI and a command line interface. Nearly all commands can be run through either one._

| Steps  | Graphic User Interface  | In Command Line  |
|---|---|---|
| __Import the .sat file into Trelis/Cubit__  | - Can be imported using the GUI with __File -> Import__. <br/></br> - Select the file through file explorer and open. <br/></br> - One important qualifier to include is `[attributes_on]`. | - In the command line the simple form of the command is `import acis [filepath]` <br/></br> - This command can be appended with further commands that can be found by typing `help import acis`. <br/></br> - These qualifiers correspond with the options given when importing files through the GUI. <br/></br> - One important qualifier to include is `[attributes_on]`.  |
| __How to save progress for the file as ACIS__  | - Click on __File -> Export__ and select the file destination and name. <br/></br> - Make sure that it is being exported as ACIS (.sat) and press ok to save.  | - In command line type `export acis [filepath] overwrite`.  |
| __Make sure units/distances are correct and if not, fix them__  | - A distance within the model of "X units" should have a metric distance of "X centimeters". <br/></br> - To check this click on a surface/line with a known metric value and then navigate to the properties page and check the surface area or curve length. <br/></br> - On the Command Panel click on __Geometry (leftmost option) -> Volume -> Transform -> Scale (from dropdown menu) -> Enter Scale Factor -> Apply__ | - A distance within the model of "X units" should have a metric distance of "X centimeters". <br/></br> - To check this in the command line the general form is `list [entity name and number] geom`. For example to check the geometry of volume 1 enter `list Volume 1 geom`. <br/></br> - In command line enter `vol all scale [Scale Factor]`. For example parts from solidworks would require `vol all scale 0.1` to convert the units to centimeters. |
| __Inspect models and resolve overlapping volumes__ | - On the Command Panel click on __Geometry (leftmost option) -> Volume -> Modify -> Heal (from dropdown menu) -> check Autoheal -> Apply__ <br/></br> - There are many options within the modify dropdown menu, but none are as robust as SpaceClaim|- In command line one can fix overlaps by typing `validate vol all` and then `healer autoheal [problem vols]`. <br/></br> - This should work to detect overlaps, but is not as robust as SpaceClaim. |

<details><p><summary>Notes</summary>
- A more general Cubit/Trelis DAGMC basics tutorial can be found at https://svalinn.github.io/DAGMC/usersguide/trelis_basics.html.
<br/></br>
- "Command Panel" and "Command Line" are necessary for GUI and command line methods respectively. To enable these select View and switch "Command Line" and/or "Command Panel" to visible.
<br/></br>
- Scale will most likely be off by a factor of 10. For example models from Solidworks will most likely be increased by 10x or 100cm to 1000 units, but this scaling changes based on the initial CAD program. You must scale every entity down or up by that factor to match units to cm.
</p></details>

#### Creation of the Graveyard

_The graveyard volume is not part of the CAD geometry being analyzed, but plays a role in the final analysis. Particles stop and are tracked once they reach the graveyard volume._

| Steps  | In Graphic User Interface  | In Command Line  |
|---|---|---|
| __Create a cube large enough to envelop all other volumes.__  | - Select __Geometry -> Volume -> Create__ and select __Brick__ from the drop down menu. <br/></br> - Type 500 in each dimension box __(width, height, depth)__ and press __Apply__ to create the block.  | - The general form is `create [shape] [dimensions based on shape]`. </br> - For a simple cube 500x500x500 you can enter `create brick x 500`.  |
| __Create another slightly larger cube to be used for graveyard.__  | - In command panel create another brick in the same way as part 1, using 750 as the new dimension in each dimension box.  | - Enter `create brick x 750`  |
| __Center volumes within the larger cubes.__  | To move the blocks in command panel select __Geometry -> Volume -> Transform__ and select __Move__ from the drop down menu. <br/></br> - Type "5 6" into the __Volume ID(s)__ box. Then __Select Method -> Distance__ and type 100 into the __X Distance__ box. _This distance/direction may vary._  | - General form is `move vol [volume ids] [axis] [distance along axis]` <br/></br> - Enter `move vol 5 6 x 100`.  |
| __Subract smaller cube from larger.__  | - Select __Geometry -> Volume -> Boolean__ and select __Subtract__ from the dropdown menu. <br/></br> - Select volume 6 as volume A and volume 5 as volume B, click __Apply__.  | - Enter `subtract vol 5 from 6`|

After this step you will be left with a large, hollow cube that can be used as a graveyard volume.

<details><p><summary>Notes</summary>
- This volumes could also be created in another CAD program with the same results, this is an example of how you could create this volumes in Trelis and Cubit.
<br/></br>
- Most likely the volumes will be slightly off centered in the x direction, but the larger bricks will be centered with one another. This may vary based on the initial CAD program.
<br/></br>
- To see the blocks better you can select the wireframe option in the top toolbar. It is directly to the right of the undo arrow on the toolbar. Also you can click on the axis on the bottom left of the volume viewing area to get a straight on (x,y) view.
-
</p></details>

#### Imprinting and Merging Volumes in Cubit/Trelis
_Imprinting and Merging surfaces accelerates the DAGMC process by combining surfaces._

  1. Imprint and Merge all shared surfaces in the model.
     * If using the GUI, in command panel select __Geometry -> Volume -> Imprint Merge__ and select __Imprint and Merge__ from the dropdown menu. Then type "all" into the __Volume ID(s)__ box and click __Apply__.
     * Otherwise in command line type `imprint volume all` and then enter. Then type `merge volume all`.
     * _Now all surfaces that previously overlapped have been merged into one surface shared by both volumes._

<details><p><summary>Notes</summary>
- The default tolerated distance for imprinting/merging surfaces is 5.0e-4 units.
<br/>
- Combining surfaces cuts two surfaces and two sets of faceting areas down to one, decreasing computational power required as well as eliminating possible errors where particles exist simultaneously in two surfaces.
</p></details>

#### Assigning Materials in Cubit/Trelis and defining the Implicit Complement
_Most commands for this section are best implemented through the command line. More general instructions can
be found_ [here](http://svalinn.github.io/DAGMC/usersguide/codes/dag-mcnp.html).

_A method (implicit complement) is implemented automatically during a DAGMC run that creates a volume in all regions of space not defined by the CAD model. By default, this volume is assumed to be a vacuum, but it can be assigned to a different material as shown below. This means that while one could explicitly create void/vacuum volumes, it is most often not necessary._

  1. The general command for assigning materials and densities in Cubit or Trelis
  `group "mat:[assigned material number]/rho:[assigned density]" add
  vol [volume numbers]` where the density is in [atoms/barn-cm] for positive values and [g/cc] for negative values.
  2. The blocks will be given two different materials and then the graveyard volume will be assigned. These material assignments will depend on the material library you create/use for the project.
     * To assign one block to the first material use `group "mat:1/rho:0.0223" add vol 1`
     * To assign the rest of the blocks (volumes 2,3,4) to the second material use `group "mat:2/rho:0.03" add vol 2 to 4`
     * To assign the graveyard volume use `group "mat:Graveyard" add vol 6`
  3. To assign a non-void/vacuum material to the implicit complement you can add the graveyard to a second material group. This second material group will be applied to the implicit complement.
     * `group "mat:3/rho:0.04" add vol 6`

#### Exporting the model to .h5m format
_The DAGMC trelis plugin translates the CAD model into a faceted model that can be used for DAGMC particle tracking. Instructions as to how to install this plugin can be found_ [here](https://svalinn.github.io/DAGMC/install/plugin.html).

  1. Once the plugin is correctly installed you should receive the message `Loaded Svalinn plugin DAGMC export command available` in the command line.
  2. Once all issues are resolved in the model, export the file as .h5m, this command must be executed through the command line.
     * The general form of the export command is `export dagmc "<filename>" [options]`. To see the options available enter `help export dagmc` into the command line.
     * The filename should include the filepath after the working directory so that it designates where the file ought to be saved after export.
     * For this part `export dagmc "~/Path/To/Folder/ErrorBlocks.h5m"` will create the part as a .h5m with default settings in the desired folder.
