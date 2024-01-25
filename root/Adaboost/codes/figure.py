import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import font_manager, rc

#mpl.rcParams.update(mpl.rcParamsDefault)
#mpl.rcParams["text.usetex"] = True
font_name = font_manager
#mpl.rcParams['font.family'] =  'Times New Roman'
mpl.rcParams['font.size'] = 12
mpl.rcParams['legend.fontsize'] = 12
# mpl.rcParams['lines.linewidth'] = 2
# mpl.rcParams['lines.linecolor'] = 'r'
# mpl.rcParams['lines.linestyle'] = '--'
# mpl.rcParams['axes.gird'] = 1
# mpl.rcParams['axes.xmargin'] = 0.1
# mpl.rcParams['axes.ymargin'] = 0.1
# mpl.rcParams['mathtext.fontset'] = "dejavuserif"
# mpl.rcParams['figure.dpi'] = 500
# mpl.rcParams['savefig.dpi'] = 500

x = np.linspace(0.001,0.999,50)

def model_w():

    # (1-x) / x > 0
    # x(1-x) > 0, x > 1, x < 1
    # x=0: 0, x=1: 0
    # x > 1, x < 1
    # x > 1: -
    # 0 < x < 1: +
    # x < 0: -

    y = 0.5*np.log((1-x)/x)

    plt.plot(x, y)
    plt.xticks(np.arange(6)*0.25)
    plt.xlim(0, 1)
    plt.ylim(-1, 1)
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')

    plt.grid(True)
    plt.xlabel('model error')
    plt.ylabel('y')
    #plt.title('alpha')
    plt.savefig('../images/alpha_t.png')
    plt.show()

def data_w():
    # plt.clf()

    z = np.sqrt((1-x)/x) # 틀린경우
    z_ = 1/z # 맞은경우
    #z = (1-x)/x

    plt.plot(x, z, color='r', label='wrong')
    plt.plot(x, z_, color='g', label='correct')
    plt.xticks(np.arange(6)*0.25)
    plt.yticks(np.arange(11)*0.2)
    plt.xlim(0.0, 1.0)
    plt.ylim(0.0, 2)
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')
    plt.grid(True)
    plt.xlabel('model error')
    plt.ylabel('y')
    #plt.title('update weight')
    plt.legend()
    plt.savefig('../images/update_w.png')
    plt.show()

model_w()
data_w()