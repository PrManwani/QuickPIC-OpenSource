import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from numpy import genfromtxt
params = {
   'axes.labelsize': 8,
   'legend.fontsize': 10,
   'xtick.labelsize': 10,
   'ytick.labelsize': 10,
   'text.usetex': False,
   'figure.figsize': [6, 4.5]
   }
rcParams.update(params)

n = 100
new = input('Do you want to change the default oscillations. Yes(1) or No(0)')
if(new==1):
	n = ('How many oscillations in one dump')

final = input('Final value of oscillations in {}s?'.format(n))
initial = input('Initial value in {}s?'.format(n))



#final values (9100 oscillations)
p3_final = genfromtxt('p3-'+str(final)+'.csv', delimiter=',')
p2_final = genfromtxt('p2-'+str(final)+'.csv', delimiter=',')
p1_final = genfromtxt('p1-'+str(final)+'.csv', delimiter=',')

x1_final = genfromtxt('x1-'+str(final)+'.csv', delimiter=',')/3.14159
x2_final = genfromtxt('x2-'+str(final)+'.csv', delimiter=',')/3.14159
x3_final = genfromtxt('x3-'+str(final)+'.csv', delimiter=',')/3.14159

#initial values (1 iteration)
p3_initial = genfromtxt('p3-'+str(initial)+'.csv', delimiter=',')
p2_initial = genfromtxt('p2-'+str(initial)+'.csv', delimiter=',')
p1_initial = genfromtxt('p1-'+str(initial)+'.csv', delimiter=',')

x1_initial = genfromtxt('x1-'+str(initial)+'.csv', delimiter=',')/3.14159
x2_initial = genfromtxt('x2-'+str(initial)+'.csv', delimiter=',')/3.14159
x3_initial = genfromtxt('x3-'+str(initial)+'.csv', delimiter=',')/3.14159

particles_i= np.shape(x1_initial)[0]
particles_f= np.shape(x1_final)[0]
print('No. of particles present initially = {}'.format(particles_i))
print('No. of particles present finally = {}'.format(particles_f))


fig = plt.figure(1)
fig.suptitle(r'Witness: After {} plasma oscillations ($\lambda_p$ = 2E-6 m), {} particles Box xmin=0  Box xmax = 3.0'.format(final*n,particles_i))

a = fig.add_subplot(221)
a.plot(x1_final,p1_final,'ro',marker = 'o',linewidth=2, label = 'Final P_x VS Final x',color='#006BB2')
a.plot(x1_initial,p1_initial,'ro',marker = 'o',linewidth=2, label = 'Initial P_x VS Initial x')
a.set_ylabel(r'$P_x$ ($\gamma$)')
a.set_xlabel(r'$x$ $(\mu m)$')
a.legend()
#plt.yscale('linear')
#plt.grid(True)


# log
b = fig.add_subplot(222)
#plt.subplot(221)
b.plot(x3_final,p3_final,'ro',marker = 'o',linewidth=2, label = 'Final P_z VS Final z',color='#006BB2')
b.plot(x3_initial,p3_initial,'ro',marker = 'o',linewidth=2, label = 'Initial P_z VS Initial z')
b.set_ylabel(r'$P_z$ ($\gamma$)')
b.set_xlabel(r'$\zeta$ $(\mu m)$')
b.legend()

d = fig.add_subplot(223)
#plt.subplot(221)
d.plot(x1_final,p3_final,'ro',marker = 'o',linewidth=2, label = 'Final P_z VS Final x',color='#006BB2')
d.plot(x1_initial,p3_initial,'ro',marker = 'o',linewidth=2, label = 'Initial P_z VS Initial x')
d.set_ylabel(r'$P_z$ ($\gamma$)')
d.set_xlabel(r'$x$ $(\mu m)$')
d.legend()
# symmetric log
c = fig.add_subplot(224)
#plt.subplot(221)
c.plot(x1_final,x3_final,'ro',marker = 'o',linewidth=2, label = 'Final z VS Final x',color='#006BB2')
c.plot(x1_initial,x3_initial,'ro',marker = 'o',linewidth=2, label = 'Initial z VS Initial x')
c.set_ylabel(r'$\zeta$ $(\mu m)$')
c.set_xlabel(r'$y$ $(\mu m)$')
c.legend()

# logit



#plt.plot(x1_20,x3_20,'ro',marker = 'o',linewidth=2, label = 'Final z VS Initial x (1000 particles)',color='#006BB2')
#plt.plot(x1_1,x3_1,'ro',marker = 'o',linewidth=2, label = 'Initial z VS Initial x (1000 particles)')
#plt.title('After {} plasma oscillations (l = 2E-3 m), Box xmin=0  Box xmax = 3.0'.format(final*100))
#plt.title('Box xmin=0, Box xmax = 3.0')
#plt.ylabel(r'$\zeta$ $(\mu m)$')
#plt.plot(x2_final,p2_final,'ro',marker = 'o',linewidth=2, label = 'Final P_y VS Final y',color='#006BB2')
#plt.plot(x2_initial,p2_initial,'ro',marker = 'o',linewidth=2, label = 'Initial P_y VS Initial y')




plt.show()
