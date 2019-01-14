import h5py
import numpy as np
import matplotlib.pyplot as plt
import os
main = '/home/pratik/hoffman/FEZ-XZ'
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
	fez = fez[u'FEZ-XZ']
	fez = fez[:,128]*1.6
	print(fez.min())
	#FEZ = np.asarray(FEZ)
	allfez.append(fez)


	#print(pathname[j])
	#FEZ[j] = FEZ[j][u'FEZ-XZ']
allfez = np.asarray(allfez)
mult = float(float(512)/float(30))
beam_pos = [round(mult*4),round(mult*6),round(mult*8),round(mult*10),round(mult*12),round(mult*14),round(mult*16),round(mult*18),round(mult*20),round(mult*22),round(mult*23.55) ]
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
f,axarr = plt.subplots(1, sharex=True, sharey=True)
plt.ylabel('TeV/m')
plt.title('9 bunches of 2.4E6 followed by 24E6 bunch and a witness bunch')
axarr.plot(allfez[0])
axarr.plot(beam_pos, [0,0,0,0,0,0,0,0,0,0,0], 'ro')
#axarr.plot(big_beam_pos, [0], 'ro', markersize= 15)
#axarr.plot(witness_pos, [0], 'rp')
'''axarr[1].plot(allfez[-1])
axarr[1].plot(beam_pos, [0,0,0,0,0,0,0,0,0,0,0], 'ro')
f.subplots_adjust(hspace=0)
for ax in axarr:
    ax.label_outer()'''
plt.show()