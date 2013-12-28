# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import os

# <codecell>

f=open('README.md','w')

prestring="""
# Matplotlib Basemap Example
Showing an example for some Matplotlib Basemap Projections
--------


## What is it for?

You can take a look at the [Basemap Documentation](http://matplotlib.org/basemap/users/), but it is not an good overview.
The following maps are created with
```
drawcountries()
drawparallels()
drawmeridians()
shadedrelief()
```
for the same area (Europe). Some projections automatically render the whole world. Some projections are missing because they need extra parameters, which are not suitable within a loop for all other.

## Projections

* 'cea' Cylindrical Equal Area
* 'mbtfpq' McBryde-Thomas Flat-Polar Quartic
* 'aeqd' Azimuthal Equidistant
* 'sinu' Sinusoidal
* 'poly' Polyconic
* 'gnom' Gnomonic
* 'moll' Mollweide
* 'lcc' Lambert Conformal
* 'tmerc' Transverse Mercator
* 'gall' Gall Stereographic Cylindrical
* 'mill' Miller Cylindrical
* 'merc' Mercator
* 'stere' Stereographic
* 'eqdc' Equidistant Conic
* 'cyl' Cylindrical Equidistant
* 'hammer' Hammer
* 'nsper' Near-Sided Perspective
* 'eck4' Eckert IV
* 'aea' Albers Equal Area
* 'kav7' Kavrayskiy VII
* 'cass' Cassini-Soldner
* 'laea' Lambert Azimuthal Equal Area
* 'robin' Robinson

## Rendering Time

![Rendering Time for the Projections](https://github.com/balzer82/BasemapExampleGallery/blob/master/BasemapRenderTimes.png?raw=true)

### Missing Projections

Not in the gallery, because extra parameters needed (mostly lat_1 or something like that)

* 'omerc' Oblique Mercator
* 'nplaea' North-Polar Lambert Azimuthal
* 'npaeqd' North-Polar Azimuthal Equidistant
* 'rotpole' Rotated Pole
* 'npstere' North-Polar Stereographic
* 'spstere' South-Polar Stereographic
* 'geos' Geostationary
* 'spaeqd' South-Polar Azimuthal Equidistant
* 'ortho' Orthographic
* 'vandg' van der Grinten (a lot of RAM needed!!)
* 'splaea' South-Polar Lambert Azimuthal


## Gallery
"""
f.write(prestring)

maps=[]
imgExts = ["png"]
for path, dirs, files in os.walk('.'):
    for fileName in files:
        ext = fileName[-3:].lower()
        if ext not in imgExts:
            continue
        else:
            maps.append('![Projection](https://github.com/balzer82/BasemapExampleGallery/blob/master/' + fileName + '?raw=true)')
            
mapstablestring='\n'.join(maps[:-1])
f.write(mapstablestring)

poststring ="""
## HTML file

Is in the Git and can be used for the own webspace to show a gallery.
"""
f.write(poststring)
f.close()

# <codecell>


