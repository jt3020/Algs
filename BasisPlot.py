import numpy as np
import sys
import os
from mpl_toolkits import mplot3d 
import matplotlib.pyplot as plt
from matplotlib import cm

##Actual 2D + 3D NURBS Basis plot

# Read in data from file
# MPLFile= open("MPL_Data", "r")
MPLFile = open('/home/jack/PhD_Work/5_IGA/c_Enhanced/Plots/MPL_Data','r')

# p and q
p = int(MPLFile.readline())
q = int(MPLFile.readline())

# refinement and total number of points
Refinement = int(MPLFile.readline())
N_Points = int(MPLFile.readline())


Position = np.zeros((N_Points,2),dtype=float)
Xi = np.zeros((Refinement),dtype=float)
Eta= np.zeros((Refinement),dtype=float)
NXi = np.zeros((Refinement,p+1),dtype=float)
NEta= np.zeros((Refinement,q+1),dtype=float)
NBi = np.zeros((Refinement,Refinement,(p+1)*(q+1)),dtype=float)

# Xi and Eta [x and y]
for point in range(Refinement):
    Line = MPLFile.readline()
    Xi[point] = float(Line)
for point in range(Refinement):
    Line = MPLFile.readline()
    Eta[point] = float(Line)

# Xi basis functions [z values for p+1 functions on x wall]
for point in range(Refinement):
    Line = MPLFile.readline()
    SplitLine = Line.split(',')
    for ii in range(p+1):
        NXi[point,ii] = float(SplitLine[ii])
# Eta basis functions [z values for q+1 functions on y wall]
for point in range(Refinement):
    Line = MPLFile.readline()
    SplitLine = Line.split(',')
    for ii in range(q+1):
        NEta[point,ii] = float(SplitLine[ii])

# Xi*Eta basis functions [sets of z values for (p+1)*(q+1) functions depending on chosen B of interest]
for ii in range(Refinement):
    for jj in range(Refinement):
        Line = MPLFile.readline()
        SplitLine = Line.split(',')
        for kk in range((p+1)*(q+1)):
            NBi[jj,ii,kk] = float(SplitLine[kk])



## 3D Plot
X, Y = np.meshgrid(Xi,Eta)
Z = NBi[:,:,4]*2

fig = plt.figure()
ax = plt.axes(projection='3d')
# ax.plot_surface(X,Y,Z,cmap=cm.coolwarm)

cp_mesh = np.zeros((12,3))

cp_mesh[0,:] = [0.0,0.0,0.0]
cp_mesh[1,:] = [0.3,0.3,0.5]
cp_mesh[2,:] = [0.3,0.7,0.5]
cp_mesh[3,:] = [0.0,1.0,0.0]

cp_mesh[4,:] = [1.0,0.0,0.0]
cp_mesh[5,:] = [0.7,0.3,0.5]
cp_mesh[6,:] = [0.7,0.7,0.5]
cp_mesh[7,:] = [1.0,1.0,0.0]

cp_mesh[8,:] = [0.3,0.3,0.5]
cp_mesh[9,:] = [0.7,0.3,0.5]

cp_mesh[10,:] = [0.3,0.7,0.5]
cp_mesh[11,:] = [0.7,0.7,0.5]

 
ax.plot(cp_mesh[0:4,0],cp_mesh[0:4,1],cp_mesh[0:4,2],linestyle='-', marker='o', color='black')

ax.plot(cp_mesh[4:8,0],cp_mesh[4:8,1],cp_mesh[4:8,2],linestyle='-', marker='o', color='black')

ax.plot(cp_mesh[8:10,0],cp_mesh[8:10,1],cp_mesh[8:10,2],linestyle='-', marker='o', color='black')

ax.plot(cp_mesh[10:12,0],cp_mesh[10:12,1],cp_mesh[10:12,2],linestyle='-', marker='o', color='black')



# test = np.zeros((101,3))
# for i in range(101):
#     test[i,:] = ( ( (cp_mesh[10,:]-cp_mesh[11,:])/100) *i ) + cp_mesh[11,:]

# ax.plot(test[:,0],test[:,1],test[:,2], color='b')


## 2D Plot
# ax.plot(Xi, NXi[:,0], zs=0, zdir='y', label='NXi_0', color='grey')
# ax.plot(Xi, NXi[:,1], zs=0, zdir='y', label='NXi_1', color='black')
# ax.plot(Xi, NXi[:,2], zs=0, zdir='y', label='NXi_2', color='grey')


# ax.plot(Eta, NEta[:,0], zs=0, zdir='x', label='NEta_0', color='grey')
# ax.plot(Eta, NEta[:,1], zs=0, zdir='x', label='NEta_1', color='black')
# ax.plot(Eta, NEta[:,2], zs=0, zdir='x', label='NEta_2', color='grey')


# x = np.linspace(0, 1, 100)
# y = np.sin(x * 2 * np.pi) / 2 + 0.5
# ax.plot(x, y, zs=0, zdir='y', label='curve in (x, y)')


# ax.set_xlabel('Xi')
# ax.set_ylabel('Eta')
# ax.set_zlabel('N')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()



# Z = NBi[:,:,4]
# fig2 = plt.figure()
# ax = plt.axes(projection='3d')
# ax.plot_surface(X,Y,Z,rstride=1, cstride=1,
#                 cmap='viridis', edgecolor='none')
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_zlabel('z');

# plt.show()



##Contour Plot
# fig = plt.figure()
# ax = plt.axes(projection='3d')

# def f(x, y):
#     return np.sin(np.sqrt(x ** 2 + y ** 2))

# x = np.linspace(-6, 6, 30)
# y = np.linspace(-6, 6, 30)

# X, Y = np.meshgrid(x, y)
# Z = f(X, Y)

# fig = plt.figure()
# ax = plt.axes(projection='3d')
# ax.contour3D(X, Y, Z, 50, cmap='binary')
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_zlabel('z');

# plt.show()


##2D + 3D Scatter
# ax = plt.figure().add_subplot(projection='3d')

# # Plot a sin curve using the x and y axes.
# x = np.linspace(0, 1, 100)
# y = np.sin(x * 2 * np.pi) / 2 + 0.5
# ax.plot(x, y, zs=0, zdir='z', label='curve in (x, y)')

# # Plot scatterplot data (20 2D points per colour) on the x and z axes.
# colors = ('r', 'g', 'b', 'k')

# # Fixing random state for reproducibility
# np.random.seed(19680801)

# x = np.random.sample(20 * len(colors))
# y = np.random.sample(20 * len(colors))
# c_list = []
# for c in colors:
#     c_list.extend([c] * 20)
# # By using zdir='y', the y value of these points is fixed to the zs value 0
# # and the (x, y) points are plotted on the x and z axes.
# ax.scatter(x, y, zs=0, zdir='y', c=c_list, label='points in (x, z)')

# # Make legend, set axes limits and labels
# ax.legend()
# ax.set_xlim(0, 1)
# ax.set_ylim(0, 1)
# ax.set_zlim(0, 1)
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')

# # Customize the view angle so it's easier to see that the scatter points lie
# # on the plane y=0
# ax.view_init(elev=20., azim=-35)

# plt.show()




