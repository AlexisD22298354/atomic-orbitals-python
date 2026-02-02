import numpy as np
import matplotlib.pyplot as plt

# Angular grid
theta = np.linspace(0, np.pi, 200)
phi = np.linspace(0, 2*np.pi, 200)
theta, phi = np.meshgrid(theta, phi)

# Angular part of p_x orbital (up to normalization)
psi = np.sin(theta) * np.cos(phi)

# Use magnitude for shape
r = np.abs(psi)

# Spherical to Cartesian
x = r * np.sin(theta) * np.cos(phi)
y = r * np.sin(theta) * np.sin(phi)
z = r * np.cos(theta)

# Plot
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(
    x, y, z,
    facecolors=plt.cm.seismic((psi - psi.min()) / (psi.max() - psi.min())),
    rstride=1, cstride=1, alpha=0.9
)

ax.set_title("pₓ orbital (angular part)")
ax.set_axis_off()
plt.show()

