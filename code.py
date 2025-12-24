import numpy as np
import matplotlib.pyplot as plt

num = int(input("How many trajectories to compare: "))

all_x = []
all_y = []

for i in range(num):

    print(f"\n--- Trajectory {i+1} ---")

    v0 = float(input("v0 (m/s): "))
    theta = float(input("angle (degree): "))
    g = float(input("gravity (m/s^2): "))
    wind_vx = float(input("Horizontal wind speed (m/s): "))
    wind_vy = float(input("Vertical wind speed (m/s): "))

    theta_rad = np.deg2rad(theta)

    # ---------- 初始速度分量 ----------
    vx = v0 * np.cos(theta_rad) + wind_vx
    vy = v0 * np.sin(theta_rad) + wind_vy

    # ---------- 時間設定 ----------
    dt = 0.01
    t = 0

    x, y = 0, 0
    x_list = [x]
    y_list = [y]

    # ---------- 運動模擬 ----------
    while y >= 0:
        x += vx * dt
        y += vy * dt
        vy -= g * dt

        x_list.append(x)
        y_list.append(y)
        t += dt

    # ---------- 儲存每一條軌跡 ----------
    all_x.append(x_list)
    all_y.append(y_list)

    print(f"Flight time: {t:.2f} s")
    print(f"Max height: {max(y_list):.2f} m")
    print(f"Range: {max(x_list):.2f} m")
plt.figure()

for i in range(num):
    plt.plot(all_x[i], all_y[i], label=f"Trajectory {i+1}")

plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Projectile Motion with Wind (Multiple Trajectories)")
plt.legend()
plt.grid()
plt.show()
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

ax.set_xlim(0, max(max(x) for x in all_x))
ax.set_ylim(0, max(max(y) for y in all_y))
max_y = max(max(y) for y in all_y)
ax.set_ylim(0, max_y * 1.1) 

lines = []
for _ in range(num):
    line, = ax.plot([], [])
    lines.append(line)

def update(frame):
    for i in range(num):
        lines[i].set_data(all_x[i][:frame], all_y[i][:frame])
    return lines

ani = FuncAnimation(fig, update, frames=3000, interval=30)
plt.title("Projectile Motion Animation")
plt.show()
