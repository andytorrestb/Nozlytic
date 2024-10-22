import numpy as np
import matplotlib.pyplot as plt
import math
import bell_nozzle

# Data from CEA results
# Chamber pressure = 130 atm
# Chamber temperature = 3781 K
# Ae/At = 13.712
# Gamma = 1.2063



class NozzleGeometry:
    def __init__(self, L_n, epsilon):
        self.L_n = L_n
        self.epsilon = epsilon
        return

    def set_radii(self):
        L_n = self.L_n
        epsilon = self.epsilon
        r_t = ((np.tan(np.pi/12)*L_n)/0.8) / (np.sqrt(epsilon) - 1)
        r_e = np.sqrt(epsilon) * r_t
        self.r_t = r_t
        self.r_e = r_e
        return r_t, r_e

    def set_nozzle_curve(self):

        # Nozzle Dimensions
        Rt = self.r_t
        Re = self.r_e
        L_n = self.L_n

        # =======================
        # ===== Throat exit =====
        # =======================
        theta_n = 3.14/3
        theta_o = -3.14/2
        theta_f = theta_n - 3.14/2

        theta = np.linspace(theta_o, theta_f, 100)
        x_throat = 0.382*Rt*np.cos(theta)
        y_throat = 0.382*Rt*np.sin(theta) + 0.382*Rt+Rt

        # =======================
        # ===== Bell/Parabolla =====
        # =======================

        # Theta values for bell nozzle are precalculated by Rao.
        theta_n = 35 * (np.pi/180) # From Rao's table
        theta_e = 10 * (np.pi/180) # From Rao's table

        # starting point (at t = 0)
        N = (x_throat[-1],y_throat[-1]) # exit point of nozzle throat equation.
        
        # ending point (at t = 1)        
        E = (L_n, Re) # exit coordinate of the nozzle

        # Control point (Q)
        m1 = np.tan(theta_n)
        m2 = np.tan(theta_e)

        C1 = N[1] - m1*N[0]
        C2 = E[1] - m2*E[0]

        Qx = (C2 - C1) / (m1 - m2)
        Qy = (m1*C2 - m2*C1) / (m1 - m2)

        Q = (Qx, Qy)


        # Plot data
        t = np.linspace(0, 1, 100)
        x_bell = (1-t)**2*N[0]+2*(1-t)*t*Q[0]+t**2*E[0]
        y_bell = (1-t)**2*N[1]+2*(1-t)*t*Q[1]+t**2*E[1]

        x = np.append(x_throat, x_bell)
        y = np.append(y_throat, y_bell)

        plt.plot(x,y)
        plt.savefig('test.png')
        return

nozzle = NozzleGeometry(1, 13.712)
print(nozzle.set_radii())
nozzle.set_nozzle_curve()