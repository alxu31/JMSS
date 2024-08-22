import matplotlib.pyplot as plt
import numpy as np

# Couldn't figure out how to plot straight from integration because the t symbol is dodgy :shurg:

t = np.linspace(0,10,100)

acceleration = 2.9830298472124213
velocity = 2.9830298472124213*t
displacement = 1.49151492360621*(t**2)

fig, axis = plt.subplots(1, 3, figsize=(10, 10))

axis[0].axhline(y = acceleration)
axis[0].set_title("Acceleration")
axis[1].plot(t, velocity)
axis[1].set_title("Velocity")
axis[2].plot(t, displacement)
axis[2].set_title("Displacement")

plt.show()