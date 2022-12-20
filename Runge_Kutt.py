from scipy.integrate import odeint, RK45, solve_ivp
import numpy as np
import matplotlib.pyplot as plt

def func(t, y, b, c):
    theta, omega = y
    dydt = [omega, -b*omega - c*np.sin(theta)]
    return dydt

b = 0.25
c = 5.0

y0 = [np.pi - 0.1, 0.0]
t = [0, 20]
sol = solve_ivp(func, t, y0, args=(b, c), method = 'RK45', dense_output=True)

t = np.linspace(0, 20, 200)
y = sol.sol(t)

plt.plot(t, y.T)
plt.legend(['theta', 'omega'], loc='best')
plt.xlabel('t')
plt.grid()
plt.show()