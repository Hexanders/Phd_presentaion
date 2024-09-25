import os
import numpy as np
import plotly.graph_objects as go

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
    
    return data, (nx, ny, nz), origin


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
    density, grid_shape, origin = read_cube(file_path)
    
    # Define the grid
    x = np.linspace(origin[0], origin[0] + grid_shape[0], grid_shape[0])
    y = np.linspace(origin[1], origin[1] + grid_shape[1], grid_shape[1])
    z = np.linspace(origin[2], origin[2] + grid_shape[2], grid_shape[2])
    X, Y, Z = np.meshgrid(x, y, z)
    
    # Create the isosurface plot
    fig = go.Figure(data=go.Isosurface(
        x=X.flatten(),
        y=Y.flatten(),
        z=Z.flatten(),
        value=density.flatten(),
        isomin=0.001,
        isomax=0.001,
        surface_count=1,
        colorscale='Viridis'
    ))

    # Set the title
    fig.update_layout(title=f"Isosurface of {cube_file}")

    # Save the plot as an HTML file
    output_path = os.path.join(output_dir, f"{os.path.splitext(cube_file)[0]}.html")
    fig.write_html(output_path)

    print(f"Saved 3D plot for {cube_file} to {output_path}")

print("All 3D plots have been saved.")
