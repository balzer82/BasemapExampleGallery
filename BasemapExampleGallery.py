# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import os
import time

# <codecell>

# Font Default
plt.rcParams.update({'font.size': 12, 'font.family': 'serif'})

# <headingcell level=2>

# Basemap Projections

# <codecell>

# Some of them are commented out because they do need some lat_1 or width or lat_0
# parameters, which do not fit the other ones
projections = [
'cea', #	Cylindrical Equal Area
'mbtfpq',#	McBryde-Thomas Flat-Polar Quartic
'aeqd',#	Azimuthal Equidistant
'sinu',#	Sinusoidal
'poly',#	Polyconic
#'omerc',#	Oblique Mercator
'gnom',#	Gnomonic
'moll',#	Mollweide
'lcc', #	Lambert Conformal
'tmerc',#	Transverse Mercator
#'nplaea',#	North-Polar Lambert Azimuthal
'gall',#	Gall Stereographic Cylindrical
#'npaeqd',#	North-Polar Azimuthal Equidistant
'mill',#	Miller Cylindrical
'merc',#	Mercator
'stere',#	Stereographic
'eqdc',#	Equidistant Conic
#'rotpole',#	Rotated Pole
'cyl', #	Cylindrical Equidistant
#'npstere',#	North-Polar Stereographic
#'spstere',#	South-Polar Stereographic
'hammer',#	Hammer
#'geos',#	Geostationary
'nsper',#	Near-Sided Perspective
'eck4',#	Eckert IV
'aea', #	Albers Equal Area
'kav7',#	Kavrayskiy VII
#'spaeqd',#	South-Polar Azimuthal Equidistant
#'ortho',#	Orthographic
'cass',#	Cassini-Soldner
#'vandg',#	van der Grinten (a lot of RAM needed!!)
'laea',#	Lambert Azimuthal Equal Area
#'splaea',#	South-Polar Lambert Azimuthal
'robin']#	Robinson

# <headingcell level=2>

# Render Map

# <codecell>

def rendermap(projection):
    '''
    For sinu, moll, hammer, npstere, spstere, nplaea, splaea, npaeqd,
    spaeqd, robin, eck4, kav7, or mbtfpq, the values of
    llcrnrlon, llcrnrlat, urcrnrlon, urcrnrlat, width and height
    are ignored (because either they are computed internally,
    or entire globe is always plotted).
    '''
    m=Basemap(llcrnrlon=-12.0, \
            llcrnrlat=32.0, \
            urcrnrlon=54.4, \
            urcrnrlat=65.3, \
            llcrnrx=None, \
            llcrnry=None, \
            urcrnrx=None, \
            urcrnry=None, \
            width=None, \
            height=None, \
            projection=projection, \
            resolution='h', \
            area_thresh=1000, \
            rsphere=6370997.0, \
            ellps=None, \
            lat_ts=None, \
            lat_1=None, \
            lat_2=None, \
            lat_0=51.0, \
            lon_0=13.0, \
            lon_1=None, \
            lon_2=None, \
            o_lon_p=None, \
            o_lat_p=None, \
            k_0=None, \
            no_rot=True, \
            suppress_ticks=True, \
            satellite_height=35786000, \
            boundinglat=None, \
            fix_aspect=True, \
            anchor='C', \
            celestial=False, \
            round=False, \
            epsg=None, \
            ax=None)
    
    m.drawcountries(linewidth=0.2, linestyle='solid', color='w', antialiased=1, ax=None, zorder=None)
    
    m.drawparallels(np.arange(-90.,120.,10.),labels=[0,0,0,0],linewidth=0.2) # draw parallels
    m.drawmeridians(np.arange(0.,420.,10.),labels=[0,0,0,0],linewidth=0.2) # draw meridians

    m.shadedrelief()

    plt.title('\'' + projection + '\' Projection', fontsize=12)
    plt.savefig(fname, dpi=300, bbox_inches='tight', transparent=True)
    plt.close()
    print('Saved \'' + fname + '\'')

# <headingcell level=2>

# Loop through all projections

# <codecell>

elapsed=dict()
for idx, projection in enumerate(projections):
    fname = 'Basemap-' + projection + '-Projection.png'
    try:
       with open(fname):
           print "Basemap #%.0f/%.0f (%s) already exist." % (idx+1, len(projections), fname)
    except IOError:
        print "Rendering Basemap #%.0f/%.0f" % (idx+1, len(projections))
        start = float(time.clock())
        rendermap(projection)
        elapsed[projection]=time.clock()-start

# <headingcell level=2>

# Render Times

# <codecell>

names = sorted(elapsed, key=elapsed.get, reverse=True)
times = sorted(elapsed.values()/np.max(elapsed.values()), reverse=True)

# <codecell>

fig = plt.figure(figsize=(16,6))
plt.bar(range(len(names)), times, align='center')
plt.xticks(range(len(elapsed)), names, rotation = 30, ha='right')
plt.title('Basemap Projections Rendering Time (relative)')
plt.grid(True)
plt.ylim([0, 1.1])
fig.savefig('BasemapRenderTimes.png',dpi=300,Transparent=True, bbox_inches='tight')
plt.close()

# <headingcell level=2>

# HTML Output

# <codecell>

f=open('BasemapGallery.html','w')

htmlintrostring = """
<html>
<head>
<title>Basemap Projections Example Gallery</title>
<style>
div { margin: 0px auto; width:800px;}
img {width: 800px;}
h1 {font-size: 30px;}
</style>
</head>
<body>
<div>
<table>
     <tr>
       <th><h1>Matplotlib Basemap Projections Example Gallery</h1></th>
     </tr>
"""
f.write(htmlintrostring)

maps=[]
imgExts = ["png"]
for path, dirs, files in os.walk('.'):
    for fileName in files:
        ext = fileName[-3:].lower()
        if ext not in imgExts:
            continue
        else:
            maps.append('\t\t<tr><td><img src="' + fileName + '"></td></tr>')
            
mapstablestring='\n'.join(maps)
f.write(mapstablestring)

htmlclosestring="""     
</table>
</div>
</body>
</html>
"""
f.write(htmlclosestring)
f.close()

# <codecell>


# <codecell>


