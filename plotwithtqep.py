import h5py
import numpy as np
import matplotlib.pyplot as plt
import os
from pylab import *

params = {
   'axes.labelsize': 8,
   'legend.fontsize': 10,
   'xtick.labelsize': 10,
   'ytick.labelsize': 10,
   'text.usetex': False,
   'figure.figsize': [6, 4.5]
   }
rcParams.update(params)

main = '/home/pratik/Desktop/Resonantcase/10_2.4E6/QEP01-XZ'
pathname = []
for file in os.listdir(main):
	if file.endswith(".h5"):
		#dprint(i)
		pathname.append(os.path.join(main, file))

pathname.sort()

allfez = []
for j, name in enumerate(pathname):
	fez = []
	fez = h5py.File(pathname[j], 'r')
	fez = fez[u'QEP01-XZ']
	fez = fez[:,128]*1.6
	print(fez.min())
	#FEZ = np.asarray(FEZ)
	allfez.append(fez)


	#print(pathname[j])
	#FEZ[j] = FEZ[j][u'FEZ-XZ']
allfez = np.asarray(allfez)
mult = float(float(512)/float(30))
beam_pos = [4,6,8,10,12,14,16,18,20,22]
#big_beam_pos = [22]
witness_pos = [23.55]
fig = plt.figure()
ax = fig.add_subplot(111)



print(np.shape(allfez))

number = np.shape(allfez)[0]
print(number)
number = number
f, axarr = plt.subplots(number, sharex=True, sharey=True)


'''#f.suptitle('Sharing both axes')
for i in range(number):
	axarr[i].plot(allfez[i])
	axarr[i].plot(beam_pos, [0,0,0,0,0,0,0,0,0,0,0], 'ro')
	axarr[i].grid(True)
# Bring subplots close to each other.
f.subplots_adjust(hspace=0)
# Hide x labels and tick labels for all but bottom plot.
for ax in axarr:
    ax.label_outer()
#plt.show()'''


#f,axarr = plt.subplots(1, sharex=True, sharey=True)

axes(frameon=0)
plt.ylabel(r'QEP ($n_o$)')
plt.xlabel(r'$\zeta$ $(\mu m)$')
#plt.title('10 bunches followed by a witness, Q~ = 2.67')
#plt.plot(number,q,marker = 'o',linewidth=2,color='#006BB2')
#lt.grid(True)
#axarr.plot(allfez[0])
plt.axhline(y=0,xmin=0,xmax=0.95, linestyle="dashed")
plt.plot(np.linspace(0,30,512),allfez[0],linewidth=2,color='#006BB2')
#axarr.plot(big_beam_pos, [0], 'ro', markersize= 15)
plt.plot(beam_pos, [0,0,0,0,0,0,0,0,0,0], 'ro')
#axarr.plot(big_beam_pos, [0], 'ro', markersize = '12')


plt.plot(witness_pos, [0], 'rp')

xticks(np.arange(0, 32, 2))

#yticks(np.arange(-1,1,0.2))
'''axarr[1].plot(allfez[-1])
axarr[1].plot(beam_pos, [0,0,0,0,0,0,0,0,0,0,0], 'ro')
f.subplots_adjust(hspace=0)
for ax in axarr:
    ax.label_outer()'''
plt.show()
