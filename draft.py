import numpy as np
I_r_width=5
I_r_height=6
I_r_grid_x = (np.arange(-I_r_width, I_r_width, 2) + 1.0) / I_r_width  # self.I_r_width
print(I_r_grid_x.shape)
I_r_grid_y = (np.arange(-I_r_height, I_r_height, 2) + 1.0) / I_r_height  # self.I_r_height
print(I_r_grid_y.shape)
g = np.meshgrid(I_r_grid_x, I_r_grid_y)
print(len(g))
P = np.stack(  # self.I_r_width x self.I_r_height x 2
            g,
            axis=2)
print(P.shape)