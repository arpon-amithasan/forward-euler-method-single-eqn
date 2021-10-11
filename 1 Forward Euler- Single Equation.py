import numpy as np
import math
import matplotlib.pyplot as plt

tn = 1000  # end time
h = 1  # step size
t = np.arange(start=0, stop=tn, step=h, dtype=float)  # time array

m0: float = 1  # initial mass
t12: float = 100  # half life
dc = math.log(2) / t12  # decay constant

m_1 = np.zeros([tn])  # array for analytical solution

m_2 = np.zeros([tn])  # array for numerical solution
m_2[0] = m0

for i in range(0, tn):  # solving decay equation analytically
    m_1[i] = m0 * math.exp(- dc * t[i])

for j in range(1, tn):  # solving decay equation numerically
    m_2[j] = m_2[j-1] + h * (-dc * m_2[j-1])

# mpl.plot(t, m_1) # plotting analytical solution
plt.plot(t, m_2)  # plotting numerical solution
plt.xlabel("seconds")
plt.ylabel("mass (kg)")
plt.title("Spontaneous nuclear decay")
plt.show()  # showing graph
