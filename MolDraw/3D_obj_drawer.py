from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from numpy import arctan, arccos, sqrt, sin, cos, array
import pickle
from collections import defaultdict, OrderedDict, namedtuple

#fig = plt.figure()
#ax = fig.gca(projection='3d')

# pos = center of mass, radius = Radius of gyration, 
#density = sites/volume
Cluster = namedtuple('Cluster', ['pos', 'radius', 'density'])

# draw sphere
'''
u, v = np.mgrid[0:2*np.pi:5j, 0:np.pi:5j]
#print(v)
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)
# alpha controls opacity
ax.plot_surface(x, y, z, color="g", alpha=0.3)
'''
'''
x0,y0,z0 = 18,12,19
R = 1
theta = arctan(y0/x0)
phi = arccos(z0/sqrt((x0*x0+y0*y0+z0*z0)))

u, v = np.mgrid[0:2*np.pi:50j, 0:np.pi:50j]
x = x0+ R*sin(v)*cos(u)
y = y0 + R*sin(u)*sin(v)
z = z0 + R*cos(v)
'''


def draw_sphere(clusters):
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')
    
    arr = array(clusters)
    #u, v = np.mgrid[0:2*np.pi:10j, 0:np.pi:10j]
    pos = arr[:,0]
    x0 = array([p[0] for p in pos])
    y0 = array([p[1] for p in pos])
    z0 = array([p[2] for p in pos])
    
    R = arr[:,1]
    S = [2*round(r*r) for r in R]
    D = arr[:,2]
    #print(R*sin(v)*cos(u))
    obj = ax.scatter(xs=x0,ys=y0,zs=z0, zdir='z', s=S, c=D, cmap='bwr')
    #plt.colorbar()
    #im = ax.imshow(S, cmap='gist_earth')
    fig.colorbar(obj, label="Site density", orientation="vertical")
    
    #density = ax.imshow(D, cmap='Blues', interpolation='none')
    #fig.colorbar(density, ax=ax)
    #fig.colorbar(mpl.cm.ScalarMappable(cmap=cmap), ax=ax)
    #plt.colorbar(label="Site density", orientation="horizontal")
    
    '''
    for cluster in clusters:
        x0,y0,z0 = cluster.pos
        R = cluster.radius *0.2 # re-scale to reduce overlap
        color = cluster.density *10 # re-scale to plot as colorbar
        u, v = np.mgrid[0:2*np.pi:50j, 0:np.pi:50j]
        x = x0 + R*sin(v)*cos(u)
        y = y0 + R*sin(u)*sin(v)
        z = z0 + R*cos(v)
        ax.plot_surface(x, y, z, color=f'{color}', alpha=0.5)
        #plt.colorbar()'''
    plt.show()
    return ax
    




file02 = 'Z:/Springsalad/sims/test_A4_B4_reference_system_SIM_FOLDER/pyStat/Cluster_density_stat/Run3_Frame_26.pickle'
pfile = open(file02, mode='rb')
clus = pickle.load(pfile)
pfile.close()

draw_sphere(clus)

