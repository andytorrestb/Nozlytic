import numpy as np
import matplotlib.pyplot as plt
import math

class NozzleGeometry:
    def __init__(self):
        return

    def set_nozzle_curve(self):

        # Nozzle exit
        Rt = 1
        theta_n = 3.14/3
        theta_o = -3.14/2
        theta_f = theta_n - 3.14/2

        theta = np.linspace(theta_o, theta_f, 100)
        x_throat = 0.382*Rt*np.cos(theta)
        y_throat = 0.382*Rt*np.sin(theta) + 0.382*Rt+Rt

        # Bell/parabola
        # starting point (at t = 0)
        P_o = (x_throat[-1],y_throat[-1])

        # Control point
        P_1 = (P_o[0] + 0.5, P_o[1] + 1.02)

        # ending point (at t = 1)        
        P_2 = (P_1[0]+2, P_1[1]+0.5)

        # Plot data
        t = np.linspace(0, 1, 100)
        x_bell = (1-t)**2*P_o[0]+2*(1-t)*t*P_1[0]+t**2*P_2[0]
        y_bell = (1-t)**2*P_o[1]+2*(1-t)*t*P_1[1]+t**2*P_2[1]

        x = np.append(x_throat, x_bell)
        y = np.append(y_throat, y_bell)

        plt.plot(x,y)
        plt.savefig('test.png')
        return



nozzle = NozzleGeometry()
nozzle.set_nozzle_curve()