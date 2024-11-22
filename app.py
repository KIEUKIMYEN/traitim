import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# Hàm tạo hình trái tim
def heart_shape(t):
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
    return x, y

# Tạo dữ liệu cho trái tim
t = np.linspace(0, 2 * np.pi, 1000)
x, y = heart_shape(t)

# Tạo ánh sáng rực rỡ xung quanh
gradient = np.linspace(0, 1, 500)
colors = LinearSegmentedColormap.from_list('glow', ['orange', 'red', 'yellow'])
gradient_colors = colors(gradient)

# Tạo hình
plt.figure(figsize=(8, 8), facecolor='black')
for i, alpha in enumerate(np.linspace(0.05, 1, 500)):
    plt.fill(x * (1 + i * 0.01), y * (1 + i * 0.01), color=gradient_colors[i], alpha=alpha)

# Vẽ trái tim chính
plt.fill(x, y, color='red', zorder=5)

# Tinh chỉnh hiển thị
plt.axis('off')  # Tắt trục
plt.gca().set_aspect('equal')  # Tỉ lệ đồng nhất
plt.show()
