import os
import numpy as np
import matplotlib.pyplot as plt

def read_cube(file_path):
    with open(file_path, 'r') as f:
        # Skip the first two comments lines
        title1 = f.readline().strip()
        title2 = f.readline().strip()
        
        # Read the atom count and origin
        natoms, *origin = map(float, f.readline().split())
        natoms = int(natoms)
        
        # Read the grid information
        nx, *xvec = map(float, f.readline().split())
        ny, *yvec = map(float, f.readline().split())
        nz, *zvec = map(float, f.readline().split())
        nx, ny, nz = int(nx), int(ny), int(nz)
        
        # Read the atom positions and charges
        atoms = []
        for _ in range(natoms):
            atom_info = list(map(float, f.readline().split()))
            atoms.append(atom_info)
        
        # Read the volumetric data
        data = []
        for line in f:
            data.extend(map(float, line.split()))
        
        data = np.array(data).reshape((nx, ny, nz))
    
    return data

# Directory containing the .cube files
cube_dir = "orbitals/"
# Output directory for the images
output_dir = "output/"

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# List all .cube files in the directory
cube_files = [f for f in os.listdir(cube_dir) if f.endswith('.cub')]
for cube_file in cube_files:
    # Read the cube file
    file_path = os.path.join(cube_dir, cube_file)
    density = read_cube(file_path)
    
    # Sum the density along one axis to get a 2D projection
    density_projection = np.sum(density, axis=0)
    
    # Normalize the density projection for better visualization
    density_projection /= np.max(density_projection)
    
    # Create the plot
    plt.imshow(density_projection, cmap='viridis', origin='lower')
    plt.colorbar(label='Density')
    
    # Set the title and labels
    plt.title(f"Density Projection of {cube_file}")
    plt.xlabel('X')
    plt.ylabel('Y')
    
    # Save the image
    output_path = os.path.join(output_dir, f"{os.path.splitext(cube_file)[0]}.png")
    plt.savefig(output_path)
    plt.close()

    print(f"Saved image for {cube_file} to {output_path}")

print("All images have been saved.")
