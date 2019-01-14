import h5py
import numpy as np
import matplotlib.pyplot as plt
import os
main = '/home/pratik/hoffman/QEP01-XZ'
pathname1 = []
for file in os.listdir(main):
	if file.endswith(".h5"):
		#dprint(i)
		pathname1.append(os.path.join(main, file))
main = '/home/pratik/hoffman/QEP02-XZ'
pathname2 = []
for file in os.listdir(main):
	if file.endswith(".h5"):
		#dprint(i)
		pathname2.append(os.path.join(main, file))


allqep1 = []
allqep2 = []
qep = []
qep = h5py.File(pathname1[0], 'r')
qep = qep[u'QEP01-XZ']
qep = qep[:,128]
print(qep.min())
#FEZ = np.asarray(FEZ)
allqep1.append(qep)

qep2 = []
qep2 = h5py.File(pathname2[0], 'r')
qep2 = qep2[u'QEP02-XZ']
qep2 = qep2[:,128]
print(qep2.min())
#FEZ = np.asarray(FEZ)
allqep2.append(qep2)

	#print(pathname[j])
	#FEZ[j] = FEZ[j][u'FEZ-XZ']
allqep1 = np.asarray(qep)
allqep2 = np.asarray(qep2)
mult = float(float(512)/float(30))
beam_pos = [round(mult*4),round(mult*6),round(mult*8),round(mult*10),round(mult*12),round(mult*14),round(mult*16),round(mult*18),round(mult*20),round(mult*22),round(mult*23.45)]
print(np.shape(allqep1))
number = np.shape(allqep1)[0]
print(np.shape(allqep2))
number = np.shape(allqep2)[0]
print(number)
number = number -16
f, axarr = plt.subplots(number, sharex=True, sharey=True)

#f.suptitle('Sharing both axes')
'''for i in range(number):
	axarr[i].plot(allqep1[i])
	axarr[i].plot(beam_pos, [0,0,0,0,0,0,0,0,0,0,0], 'ro')
# Bring subplots close to each other.
f.subplots_adjust(hspace=0)'''
# Hide x labels and tick labels for all but bottom plot.
'''for ax in axarr:
    ax.label_outer()
#plt.show()'''
f, axarr = plt.subplots(2, sharex=True, sharey=True)
axarr[0].plot(allqep1)
axarr[0].plot(beam_pos, [0,0,0,0,0,0,0,0,0,0,0], 'ro')
axarr[1].plot(allqep2)
axarr[1].plot(beam_pos, [0,0,0,0,0,0,0,0,0,0,0], 'ro')
f.subplots_adjust(hspace=0)
'''for ax in axarr:
    ax.label_outer()'''
plt.show()
