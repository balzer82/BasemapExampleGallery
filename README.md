
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
![Projection](https://github.com/balzer82/BasemapExampleGallery/blob/master/Basemap-aea-Projection.png?raw=true)
![Projection](https://github.com/balzer82/BasemapExampleGallery/blob/master/Basemap-aeqd-Projection.png?raw=true)
![Projection](https://github.com/balzer82/BasemapExampleGallery/blob/master/Basemap-cass-Projection.png?raw=true)
![Projection](https://github.com/balzer82/BasemapExampleGallery/blob/master/Basemap-cea-Projection.png?raw=true)
![Projection](https://github.com/balzer82/BasemapExampleGallery/blob/master/Basemap-cyl-Projection.png?raw=true)
![Projection](https://github.com/balzer82/BasemapExampleGallery/blob/master/Basemap-eck4-Projection.png?raw=true)
![Projection](https://github.com/balzer82/BasemapExampleGallery/blob/master/Basemap-eqdc-Projection.png?raw=true)
![Projection](https://github.com/balzer82/BasemapExampleGallery/blob/master/Basemap-gall-Projection.png?raw=true)
![Projection](https://github.com/balzer82/BasemapExampleGallery/blob/master/Basemap-gnom-Projection.png?raw=true)
![Projection](https://github.com/balzer82/BasemapExampleGallery/blob/master/Basemap-hammer-Projection.png?raw=true)
![Projection](https://github.com/balzer82/BasemapExampleGallery/blob/master/Basemap-kav7-Projection.png?raw=true)
![Projection](https://github.com/balzer82/BasemapExampleGallery/blob/master/Basemap-laea-Projection.png?raw=true)
![Projection](https://github.com/balzer82/BasemapExampleGallery/blob/master/Basemap-lcc-Projection.png?raw=true)
![Projection](https://github.com/balzer82/BasemapExampleGallery/blob/master/Basemap-mbtfpq-Projection.png?raw=true)
![Projection](https://github.com/balzer82/BasemapExampleGallery/blob/master/Basemap-merc-Projection.png?raw=true)
![Projection](https://github.com/balzer82/BasemapExampleGallery/blob/master/Basemap-mill-Projection.png?raw=true)
![Projection](https://github.com/balzer82/BasemapExampleGallery/blob/master/Basemap-moll-Projection.png?raw=true)
![Projection](https://github.com/balzer82/BasemapExampleGallery/blob/master/Basemap-nsper-Projection.png?raw=true)
![Projection](https://github.com/balzer82/BasemapExampleGallery/blob/master/Basemap-poly-Projection.png?raw=true)
![Projection](https://github.com/balzer82/BasemapExampleGallery/blob/master/Basemap-robin-Projection.png?raw=true)
![Projection](https://github.com/balzer82/BasemapExampleGallery/blob/master/Basemap-sinu-Projection.png?raw=true)
![Projection](https://github.com/balzer82/BasemapExampleGallery/blob/master/Basemap-stere-Projection.png?raw=true)
![Projection](https://github.com/balzer82/BasemapExampleGallery/blob/master/Basemap-tmerc-Projection.png?raw=true)
## HTML file

Is in the Git and can be used for the own webspace to show a gallery.
