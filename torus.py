import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

R = 1
r = 1
z_flattening_factor = 0.4

u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, 2 * np.pi, 100)
u, v = np.meshgrid(u, v)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.set_box_aspect([1, 1, z_flattening_factor])

def calculate_torus(R, r, u, v, time, rotation_speed=0.1):
    u_rot = u
    v_rot = v + rotation_speed * time
    x = (R + r * np.cos(v_rot)) * np.cos(u_rot)
    y = (R + r * np.cos(v_rot)) * np.sin(u_rot)
    z = r * np.sin(v_rot) * z_flattening_factor
    return x, y, z

time = 0
x, y, z = calculate_torus(R, r, u, v, time)
surface = ax.plot_surface(x, y, z, cmap='viridis', edgecolor='none')

def update(frame):
    x, y, z = calculate_torus(R, r, u, v, frame)
    ax.clear()
    ax.plot_surface(x, y, z, cmap='viridis', edgecolor='none')
    ax.set_title("Outward Rotational Flow Horn Torus")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")
    ax.set_box_aspect([1, 1, z_flattening_factor])

anim = FuncAnimation(fig, update, frames=200, interval=50)

plt.show()
