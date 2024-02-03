import numpy as np
import matplotlib.pyplot as plt

def generate_multibrot(width, height, max_iter, seed_val):
    # Generate initial entropy
    entropy = np.random.rand(seed_val)

    # Determine parameters based on entropy
    color_map = np.random.choice(['hot', 'cool', 'rainbow', 'flag', 'prism', 'ocean', 'terrain', 'gnuplot', 'gnuplot2', 'cubehelix', 'gist_rainbow', 'jet', 'turbo', 'nipy_spectral', 'gist_ncar']) #https://www.analyticsvidhya.com/blog/2020/09/colormaps-matplotlib/
    size = np.random.randint(200, 600)
    #pattern = np.random.choice(['circle', 'triangle', 'square', ])
    #pattern = np.random.choice(['circle', 'triangle', 'square', 'pentagon', 'hexagon', 'heptagon', 'octagon', 'nonagon', 'decagon', 'hendecagon', 'dodecagon'])
    pattern = np.random.randint(3,5)

    # Generate the Multibrot fractal
    real_vals = np.linspace(-2, 2, width)
    imag_vals = np.linspace(-2, 2, height)
    multibrot = np.zeros((width, height))

    for i in range(width):
        for j in range(height):
            c = complex(real_vals[i], imag_vals[j])
            z = 0
            for k in range(max_iter):
                if abs(z) > 2:
                    break
                z = z ** pattern + c

            multibrot[i, j] = k

    return multibrot, color_map, size, pattern

# Set the parameters
width = 800
height = 800
max_iter = 256

seed_val = np.random.randint(0,99)

# Generate the Multibrot fractal
multibrot, color_map, size, pattern = generate_multibrot(width, height, max_iter, seed_val)

# Display the fractal
plt.figure(figsize=(size/100, size/100))
plt.imshow(multibrot.T, cmap=color_map, extent=[-2, 2, -2, 2])
plt.title("Multibrot Fractal")
plt.xlabel("Real")
plt.ylabel("Imaginary")
plt.show()

