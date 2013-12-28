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
            
mapstablestring='\n'.join(maps)
f.write(mapstablestring)

poststring ="""
## HTML file

Is in the Git.
"""
f.write(poststring)
f.close()

# <codecell>


