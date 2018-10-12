from matplotlib import pyplot
import matplotlib as mpl
import numpy as np

fig = pyplot.figure(2)

# make values from -5 to 5, for this example
zvals = np.random.rand(100,100)*10-5

# make a color map of fixed colors
cmap = mpl.colors.ListedColormap(['blue','black','red'])
bounds=[-6,-2,2,6]
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

cmap2 = mpl.colors.LinearSegmentedColormap.from_list('my_colormap',
                                           ['blue','black','red'],
                                           256)

# tell imshow about color map so that only set colors are used
img = pyplot.imshow(zvals,interpolation='nearest',
                    cmap = cmap,norm=norm)

img2 = pyplot.imshow(zvals,interpolation='nearest',
                    cmap = cmap2,
                    origin='lower')

# make a color bar
pyplot.colorbar(img,cmap=cmap,
                norm=norm,boundaries=bounds,ticks=[-5,0,5])

pyplot.colorbar(img2,cmap=cmap2)

pyplot.show()