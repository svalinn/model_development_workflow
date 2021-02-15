# Two Slab Model
![viewshieldblock701](viewshieldblock701.png)<br/></br>
The simple two slab model geometry consists of two slabs and a cube that holds an isotropic 14 MeV source.
#### Goals of Example

  * Use the UW2 workflow
  * Use a simple PyNE script to make materials
  * Use a Cubit/Trelis script to create the model and prepare it for DAGMC
  * Inject materials into the h5m faceted geometry file for transport
  * Run dag-mcnp6 with the CAD model prepared above

#### Procedure Overview

  1. Create materials by running a simple python PyNE script
  2. Create the two slab model and prepare it for DAGMC by running a Cubit/Trelis journal script
  3. Run uwuw_preproc to inject materials into h5m faceted geometry file
  4. Run DAG-MCNP62 using the supplied input file

_Cubit is a meshing pre-processing software with CAD capabilities and Trelis is the commercially available version. It is used in this workflow to create the CAD model, assign materials to volumes, and finally export the model to the faceted DAGMC .h5m format._<br/></br>
_Preparing and exporting the model to a faceted h5m format requires Cubit/Trelis and the DAGMC Cubit/Trelis plugin, which should be installed before starting the tutorial. Instructions are [here](https://svalinn.github.io/DAGMC/install/plugin.html)._

## Procedure:

### In the bash command shell type:
\>/path/to/[makeMatls.py](makeMatls.py) <br/></br>
This will create the materials used in this particular calculation (iron, water) and write a PyNE material database file in h5m format (filename=twoslab_matlLib.h5m).  It will also write a file in mcnp material card format in case the user wants to examine the materials before continuing with the tutorial workflow (filename=twoslab_mcard.txt).

_Installing the PyNE package for python is required to use this particular python script. Instructions are [here](https://pyne.io/)._

### In the Cubit/Trelis command/journal script prompt type:
\>playback '/path/to/[prepareshieldmodeltrelis701.jou](prepareshieldmodeltrelis701.jou)' <br/></br>
This will create the two slabs, the cube, and the graveyard. It will check for CAD errors, then imprint and merge the model.  Next it will assign materials and finally facet, make_watertight, and export the model in h5m format (filename=shieldblock701_zip.h5m).



### In the bash command shell type:
\>/path/to/uwuw_preproc shieldblock701_zip.h5m -v -l twoslab_matlLib.h5m <br/></br>
This will inject the materials into the faceted h5m geometry file for the Monte Carlo transport calculation.

### In the bash command shell type:
\>/path/to/dag-mcnp62 n=[shieldblock701](shieldblock701) gcad=shieldblock701_zip.h5m lcad=shieldblock701.glist <br/></br>
This will run dag-mcnp6 using the two slab model and materials that were prepared in the previous step. You can compare your tally results to ours using the mcnp [mctal file](shieldblock701m).
