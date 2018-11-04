#https://stackoverflow.com/questions/13784201/matplotlib-2-subplots-1-colorbar

from mpl_toolkits.axes_grid1 import ImageGrid

# Set up figure and image grid
#fig = plt.figure(figsize=(9.75, 3))
fig = plt.figure(figsize=(15, 15))

grid = ImageGrid(fig, 121,          # as in plt.subplot(111)
                 nrows_ncols=(3,3),
                 axes_pad=0.15,
                 share_all=True,
#                  cbar_location="right",
#                  cbar_mode="single",
#                  cbar_size="7%",
#                  cbar_pad=0.15,
                 )

# Add data to image grid
for ax in grid:
    im = ax.scatter(X,Y, s=50, c=T, alpha=.8, cmap='RdYlGn')
    ax.axis('off')

# Colorbar
#ax.cax.colorbar(im)
#ax.cax.toggle_label(True)

grid = ImageGrid(fig, 122,          # as in plt.subplot(111)
                 nrows_ncols=(3,3),
                 axes_pad=0.15,
                 share_all=True,
                 cbar_location="right",
                 cbar_mode="single",
                 cbar_size="7%",
                 cbar_pad=0.15,
                 )

# Add data to image grid
for ax in grid:
    #im = ax.imshow(np.random.random((10,10)), vmin=0, vmax=1)
    im = ax.scatter(X,Y, s=5, c=T, alpha=.8)
    ax.axis('off')

# Colorbar
ax.cax.colorbar(im)
ax.cax.toggle_label(True)

#plt.tight_layout()    # Works, but may still require rect paramater to keep colorbar labels visible
plt.savefig('output.png', bbox_inches='tight')
# plt.axis('off')
# fig = plt.gcf()
# fig.set_size_inches(7.0/3, 7.0/3) #dpi = 300, output = 700*700 pixels
# plt.gca().xaxis.set_major_locator(plt.NullLocator())
# plt.gca().yaxis.set_major_locator(plt.NullLocator())
# plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, hspace = 0, wspace = 0)
# plt.margins(0,0)
# fig.savefig('output.png', format='png', transparent=True, dpi=300, pad_inches = 0)
plt.show()





import numpy as np
import matplotlib.pyplot as plt

n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)
T = np.arctan2(Y,X)

X = []
Y = []
T = []
for x in range(-5, 6):
    for y in range(-5, 6):
        if abs(x) + abs(y) > 7: continue
        X.append(x)
        Y.append(y)
        T.append(np.random.rand())

X = np.array(X)
Y = np.array(Y)
T = np.array(T)

plt.figure()
#plt.axes([0.025,0.025,0.95,0.95])
plt.scatter(X,Y, s=200, c=T, alpha=.8)

plt.xlim(-6,6)
#plt.xticks([])
plt.ylim(-6,6)
#plt.yticks([])
# savefig('../figures/scatter_ex.png',dpi=48)

plt.colorbar()
plt.show()

fig = plt.figure(figsize=(5, 10))

#plt.subplots_adjust(hspace=0.6, wspace=0.4)
plt.subplot(3,2,1)
plt.scatter(X,Y, s=20, c=T, alpha=.8)
plt.xlim(-6,6)
plt.ylim(-6,6)
plt.xticks([])
plt.yticks([])
plt.axis('off')

plt.subplot(3,2,2)
plt.scatter(X,Y, s=20, c=T, alpha=.8)
plt.xlim(-6,6)
plt.ylim(-6,6)
plt.axis('off')

plt.subplot(3,2,3)
plt.scatter(X,Y, s=20, c=T, alpha=.8)
plt.xlim(-6,6)
plt.ylim(-6,6)
plt.axis('off')

plt.subplot(3,2,4)
plt.scatter(X,Y, s=20, c=T, alpha=.8)
plt.xlim(-6,6)
plt.ylim(-6,6)
plt.axis('off')

plt.subplot(3,2,5)
plt.scatter(X,Y, s=20, c=T, alpha=.8)
plt.xlim(-6,6)
plt.ylim(-6,6)
plt.axis('off')

plt.subplot(3,2,6)
plt.scatter(X,Y, s=20, c=T, alpha=.8)
plt.xlim(-6,6)
plt.ylim(-6,6)
plt.axis('off')

fig.subplots_adjust(right=0.8)
#cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
fig.colorbar(im, cax=cbar_ax)

plt.savefig('test01.png')
plt.show()
