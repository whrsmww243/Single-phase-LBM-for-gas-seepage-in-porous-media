import numpy as np
import matplotlib.pyplot as plt

size=1000
width=10
spacing=30
amplitude=10
frequency=0.01

def generate_curved_channels(size, width, spacing, amplitude, frequency):
    """Generate sinusoidal curved flow channels, maintaining the same number as the straight channels"""
    grid = np.ones((size, size))
    
    # Use the same layout parameters as the straight channel
    channel_count = (size - width) // spacing
    start_pos = (size - (channel_count * spacing + width)) // 2
    
    for row in range(size):
        # Sine wave parameters (one complete cycle)
        sin_offset = int(amplitude * np.sin(row * 2*np.pi/(size/16)))
        
        # Generate curved flow channels
        for i in range(start_pos + spacing//2, size, spacing):
            left = max(0, i + sin_offset - width//2)
            right = min(size, i + sin_offset + width//2)
            
            # Ensure minimum effective width
            if right - left >= width//2:
                grid[row, left:right] = 0
    
    # Boundary protection
    #grid[0, :] = 1; grid[-1, :] = 1; grid[:, 0] = 1; grid[:, -1] = 1
    return grid

curved_grid = generate_curved_channels(size, width, spacing, amplitude, frequency)
#curved_grid = np.rot90(curved_grid)

# Add inlet and outlet transition layers
zeros_row = np.zeros((5,size))
curved_grid = np.vstack([zeros_row,curved_grid,zeros_row])
curved_grid = np.rot90(curved_grid)

plt.figure(figsize=(8, 8))
curved_grid = np.ma.masked_where((curved_grid > 0.0), curved_grid)
plt.imshow(curved_grid, vmin= -1.0,
                    vmax= 1.0, aspect='auto', interpolation='nearest')


filename = 'curved_'+str(size)+'_'+str(spacing)+'_16'
plt.axis('off')
plt.savefig(filename+'_rot90'+'.png', dpi=300 ,bbox_inches='tight', pad_inches=0)
#plt.show()

# Flattening matrix (row priority)
flat_curved = curved_grid.flatten()

# Save txt file
np.savetxt(filename+'_rot90'+'.txt', flat_curved, fmt="%d") 

