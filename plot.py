import matplotlib.pyplot as plt
import scipy as sp
import numpy as np
import matplotlib as mpl
from matplotlib.colors import LogNorm
from matplotlib import colors

class MidpointNormalize(mpl.colors.Normalize):
    def __init__(self, vmin, vmax, midpoint=0, clip=False):
        self.midpoint = midpoint
        mpl.colors.Normalize.__init__(self, vmin, vmax, clip)

    def __call__(self, value, clip=None):
        normalized_min = max(0.0, 1.0 / 2.0 * (1.0 - abs((self.midpoint - self.vmin) / (self.midpoint - self.vmax))))
        normalized_max = min(1.0, 1.0 / 2.0 * (1.0 + abs((self.vmax - self.midpoint) / (self.midpoint - self.vmin))))
        normalized_mid = 0.5
        x, y = [self.vmin, self.midpoint, self.vmax], [normalized_min, normalized_mid, normalized_max]
        return sp.ma.masked_array(sp.interp(value, x, y))


# offset = 174
offset_min = 300
offset_max = 140

def pix_to_lenght( pix ):
    return pix / 431 * 5

filename = "raw_0138ns"
# filename = "raw_0262ns"
# filename = "raw_0388ns"
# filename = "raw_1010ns"
# filename = "raw_3140ns"

with open( filename + ".asc" ) as file_in:
    lines = []
    lines2 = []
    for line in file_in:
        # floats = [ ( float(x) * 9.596E22/6.283 if float(x) > 0 else float(x) * 4.2E17/6.283 ) for x in line.split()]
        floats = [ ( float(x) * 9.596E22/6.283 if float(x) > 0 else 0 ) for x in line.split()]
        # floats = [ ( float(x) * 4.2E17/6.283 if float(x) < 0 else 0 ) for x in line.split()]
        # floats = [ float(x) for x in line.split()]
        lines.append( floats )
        # cleanedList = [float(x) for x in floats if str(x) != 'nan']
        # if ( len(cleanedList) > 0 ):
        #     lines.append( floats[offset_min : len(floats)-offset_max] )

lines = np.flip(lines, 0)

Z = lines
z = Z
# z_min, z_max = -np.nanmax(np.abs(z)), np.nanmax(np.abs(z))
z_min, z_max = -np.nanmax(np.abs(z)), np.nanmax(np.abs(z))
# z_min, z_max = np.nanmin(z), np.nanmax(z)
# z_min, z_max = -np.abs(lines).max(), np.abs(lines).max()

print("z_min ")
print(z_min)
print("z_max ")
print(z_max)


z_min, z_max = -6.5e+22, 6.5e+22
# z_min, z_max = -9e+17, 9e+17

fig, (ax0) = plt.subplots(1, 1, figsize=(10, 8) )

# c = ax0.pcolor(Z, cmap='bwr', vmin=z_min, vmax=z_max)

# norm = MidpointNormalize(vmin=z_min, vmax=z_max, midpoint=0.0)

c = ax0.imshow(Z, cmap='bwr', vmin=z_min, vmax=z_max, # norm=norm,
              extent=[ 0, pix_to_lenght( z.shape[1] ), 0, pix_to_lenght( z.shape[0] ) ],
              interpolation='nearest', origin='lower')
ax0.set_xlabel('Lenght (mm)')
ax0.set_ylabel('Lenght (mm)')

# cmap colors:
# viridis
# plasma
# magma
# y mas aca: https://matplotlib.org/tutorials/colors/colormaps.html
ax0.set_title( filename )
fig.colorbar(c, ax=ax0)

# c = ax1.pcolor(Z, edgecolors='k', linewidths=4)
# ax1.set_title('thick edges')

fig.tight_layout()
plt.show()


