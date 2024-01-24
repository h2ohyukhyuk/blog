import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0.001,0.999,50)
print(x)
# (1-x) / x > 0
# x(1-x) > 0, x > 1, x < 1
# x=0: 0, x=1: 0
# x > 1, x < 1
# x > 1: -
# 0 < x < 1: +
# x < 0: -

y = 0.5*np.log((1-x)/x)
print(y)

plt.plot(x, y)
plt.xticks(np.arange(11)*0.1)
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.title('alpha')
plt.savefig('../images/alpha_t.png')
#plt.show()
plt.clf()

z = np.exp(2*y)
#z = (1-x)/x

plt.plot(x, z)
plt.xticks(np.arange(11)*0.1)
plt.yticks(np.arange(101))
plt.ylim(-0.01, 10)
plt.grid(True)
plt.xlabel('x')
plt.ylabel('z')
plt.title('exp')
plt.savefig('../images/exp_a.png')
plt.show()






