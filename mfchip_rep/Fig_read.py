import numpy as np
import matplotlib.pyplot as plt

def txt_to_image(input_txt, original_width, original_height, output_image):
    # Read data from txt file and convert to numpy array
    with open(input_txt, 'r') as f:
        data = np.array([int(line.strip()) for line in f])
    
    # Reshaping two-dimensional matrix to the original image size
    binary_matrix = data.reshape((original_height, original_width))
    
    # Show image
    plt.imshow(binary_matrix, cmap='gray', vmin=0, vmax=1)
    plt.axis('off')
    plt.title(f"Reconstructed Image ({original_width}x{original_height})")
    
    # Save image
    plt.savefig(output_image, bbox_inches='tight', pad_inches=0)
    plt.show()

# Replace with the actual original image size
txt_to_image('output2.txt', original_width=2046, original_height=1252, output_image='Ex_comparison3.png')
