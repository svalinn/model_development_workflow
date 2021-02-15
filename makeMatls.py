#!/usr/bin/python
#
from pyne.material import Material,MaterialLibrary
print "Welcome!"
mat_lib=MaterialLibrary()
#
# define iron for a shield
ironvec={260000:1} # pure iron
iron=Material()
iron.density=7.86
iron.from_atom_frac(ironvec)
iron=iron.expand_elements()
# to write out an mcnp material card
iron.metadata['mat_number']=101
iron.write_mcnp('twoslab_mcard.txt', 'atom')
#
#
# define a simple water since O-18 not in mcnp xs libs
watervec={10010000:2,80160000:1} # simple water
water = Material()
water.density = 1.0
water.from_atom_frac(watervec)
# to write out an mcnp material card
water.metadata['mat_number']=102
water.write_mcnp('twoslab_mcard.txt', 'atom')
#
# define a low density simple water since O-18 not in mcnp xs libs
watervec={10010000:2,80160000:1} # simple water
lowdensitywater = Material()
lowdensitywater.density = 0.9
lowdensitywater.from_atom_frac(watervec)
# to write out an mcnp material card
lowdensitywater.metadata['mat_number']=103
lowdensitywater.write_mcnp('twoslab_mcard.txt', 'atom')
#
mat_lib["Iron"]=iron
mat_lib["Water"]=water
mat_lib["lowdensityWater"]=lowdensitywater
#
mat_lib.write_hdf5("twoslab_matlLib.h5m") # writes to default datapath
                                      # appends to matl library if already exists
# change datapath to be able to read with older version of uwuw_preproc
#mat_lib.write_hdf5("twoslab_matlLib_old.h5m",datapath='/materials', nucpath='/nucid')
#
print "All done!"
