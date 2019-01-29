import h5py
import numpy as np
import matplotlib.pyplot as plt
import os

main = '/home/pratik/hoffman/RAW-BEAM/11'
datapath = '/home/pratik/hoffman/beam'
'''
pathname = []
for file in os.listdir(main):
	print(file)
	for subfile in os.listdir(main+'/'+file):
		print(subfile)
		if subfile.endswith(".h5"):
			#dprint(i)
			pathname.append(os.path.join(main,file,subfile))
			'''

pathname = []
for file in os.listdir(main):
	if file.endswith(".h5"):
		#dprint(i)
		pathname.append(os.path.join(main,file))

pathname.sort()
print(pathname)

for j, name in enumerate(pathname):
	beam = []
	with h5py.File(pathname[j],'r') as f:
		p1 = f[u'p1']
		p2 = f[u'p2']
		p3 = f[u'p3']
		p1 = f[u'x1']
		x2 = f[u'x2']
		x3 = f[u'x3']
		data_p1 = f['p1']
		data_p2 = f['p2']
		data_p3 = f['p3']
		data_x1 = f['x1']
		data_x2 = f['x2']
		data_x3 = f['x3']
		#data_p1 = data_p[0]
		#print((np.shape(data_p1)))
		#print(data_p1[:])
		path_p1 = datapath + '/'+ "p1-"+str(j+1)+'.csv'
		path_p2 = datapath + '/'+ "p2-"+str(j+1)+'.csv'
		path_p3 = datapath + '/'+ "p3-"+str(j+1)+'.csv'
		path_x1 = datapath + '/'+ "x1-"+str(j+1)+'.csv'
		path_x2 = datapath + '/'+ "x2-"+str(j+1)+'.csv'
		path_x3 = datapath + '/'+ "x3-"+str(j+1)+'.csv' 
		np.savetxt(path_p1, data_p1[:], delimiter=",")
		np.savetxt(path_p2, data_p2[:], delimiter=",")
		np.savetxt(path_p3, data_p3[:], delimiter=",")
		np.savetxt(path_x1, data_x1[:], delimiter=",")
		np.savetxt(path_x2, data_x2[:], delimiter=",")
		np.savetxt(path_x3, data_x3[:], delimiter=",")
	#print(beam)
