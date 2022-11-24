import this

from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque
import matplotlib.path as mpath
import matplotlib.patches as mpatches

class Graph:
    G = 9.8  # acceleration due to gravity, in m/s^2
    L1 = 1.0  # length of pendulum 1 in m
    L2 = 1.0  # length of pendulum 2 in m
    L = L1 + L2  # maximal length of the combined pendulum
    M1 = 1.0  # mass of pendulum 1 in kg
    M2 = 1.0  # mass of pendulum 2 in kg
    t_stop = 7.5  # how many seconds to simulate
    history_len = 500  # how many trajectory points to display

    def __init__(self):
        print("hello world")
        # create a time array from 0..t_stop sampled at 0.02 second steps
        self.dt = 0.01
        self.t = np.arange(0, self.t_stop, self.dt)

        # th1 and th2 are the initial angles (degrees)
        # w10 and w20 are the initial angular velocities (degrees per second)
        self.th1 = 120.0
        self.w1 = 0.0
        self.th2 = -10.0
        self.w2 = 0.0

        # initial state
        self.state = np.radians([self.th1, self.w1, self.th2, self.w2])

        # integrate the ODE using Euler's method
        self.y = np.empty((len(self.t), 4))
        self.y[0] = self.state
        for i in range(1, len(self.t)):
            self.y[i] = self.y[i - 1] + self.derivs(self.t[i - 1], self.y[i - 1]) * self.dt

        # A more accurate estimate could be obtained e.g. using scipy:
        #
        #   y = scipy.integrate.solve_ivp(derivs, t[[0, -1]], state, t_eval=t).y.T

        self.x1 = self.L1 * sin(self.y[:, 0])
        self.y1 = -self.L1 * cos(self.y[:, 0])

        self.x2 = self.L2 * sin(self.y[:, 2]) + self.x1
        self.y2 = -self.L2 * cos(self.y[:, 2]) + self.y1

        self.fig = plt.figure(figsize=(5, 4))
        self.ax = self.fig.add_subplot(autoscale_on=False, xlim=(-self.L, self.L), ylim=(-self.L, 1.))
        self.ax.set_aspect('equal')
        self.ax.grid()

        self.line, = self.ax.plot([], [], 'o-', lw=2)
        self.trace, = self.ax.plot([], [], '.-', lw=1, ms=2)
        self.time_template = 'time = %.1fs'
        self.time_text = self.ax.text(0.05, 0.9, '', transform=self.ax.transAxes)
        self.history_x, self.history_y = deque(maxlen=self.history_len), deque(maxlen=self.history_len)

    def derivs(self, t, state):
        dydx = np.zeros_like(state)

        dydx[0] = state[1]


        delta = state[2] - state[0]
        den1 = (self.M1 + self.M2) * self.L1 - self.M2 * self.L1 * cos(delta) * cos(delta)
        dydx[1] = ((self.M2 * self.L1 * state[1] * state[1] * sin(delta) * cos(delta)
                    + self.M2 * self.G * sin(state[2]) * cos(delta)
                    + self.M2 * self.L2 * state[3] * state[3] * sin(delta)
                    - (self.M1 + self.M2) * self.G * sin(state[0]))
                   / den1)

        dydx[2] = state[3]

        den2 = (self.L2 / self.L1) * den1
        dydx[3] = ((- self.M2 * self.L2 * state[3] * state[3] * sin(delta) * cos(delta)
                    + (self.M1 + self.M2) * self.G * sin(state[0]) * cos(delta)
                    - (self.M1 + self.M2) * self.L1 * state[1] * state[1] * sin(delta)
                    - (self.M1 + self.M2) * self.G * sin(state[2]))
                   / den2)

        return dydx

    def animate(self,i):
        self.thisx = [0, self.x1[i], self.x2[i]]
        self.thisy = [0, self.y1[i], self.y2[i]]

        if i == 0:
            self.history_x.clear()
            self.history_y.clear()

        self.history_x.appendleft(self.thisx[2])
        self.history_y.appendleft(self.thisy[2])

        self.line.set_data(self.thisx, self.thisy)
        self.trace.set_data(self.history_x, self.history_y)
        self.time_text.set_text(self.time_template % (i * self.dt))
        return self.line, self.trace, self.time_text

    def show(self):
        ani = animation.FuncAnimation(
            self.fig, self.animate, len(self.y), interval=self.dt * 1000, blit=True)
        plt.show()

class Graph2:

    def __init__(self):
        Path = mpath.Path

        fig, ax = plt.subplots()
        pp1 = mpatches.PathPatch(
            Path([(0, 0), (1, 0), (1, 1), (0, 0)],
                 [Path.MOVETO, Path.CURVE3, Path.CURVE3, Path.CLOSEPOLY]),
            fc="none", transform=ax.transData)

        ax.add_patch(pp1)
        ax.plot([0.75], [0.25], "ro")
        ax.set_title('The red point should be on the path')

        plt.show()