import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------
# Phase Visualization Demo
# -----------------------------------
# Educational ONLY — demonstrates basic
# optical phase structure without any
# proprietary methods.
# -----------------------------------

# Grid setup
N = 400
x = np.linspace(-5, 5, N)
y = np.linspace(-5, 5, N)
X, Y = np.meshgrid(x, y)

# Phase calculation
phase = np.arctan2(Y, X)

# Display
plt.figure(figsize=(6,6))
plt.imshow(phase, cmap='twilight', extent=(-5,5,-5,5))
plt.title("Basic Optical Phase Map\n(arctan2(y, x))")
plt.colorbar(label="Phase (radians)")
plt.axis("off")
plt.show()
