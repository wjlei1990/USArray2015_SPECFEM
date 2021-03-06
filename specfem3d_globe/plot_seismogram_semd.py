##########################################
#This script is used to plotting the semd file generated by the specfem2d
#Put this script in the code home directory if you don't the path
##########################################

import matplotlib as mpl
mpl.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
import os
import glob

# !!!!!!!!!!!!!!!!!!!!!!!
# the directory where you put the semd file
OUTPUTDIR = "./OUTPUT_FILES"

# generate the semd filelist
filelist = glob.glob(os.path.join(OUTPUTDIR, "*.sem.ascii"))
print "Number of semd filelist:", len(filelist)
if len(filelist) == 0:
    print "No semd files found. Please check your OUTPUTDIR path:%s" %OUTPUTDIR

# plot every semd file
for filename in filelist:
    print "----------\n"
    print "Plotting semd file: %s" % filename
    basename = os.path.basename(filename)
    outputfig = os.path.join(OUTPUTDIR, "%s.png" % basename)
    print "Output figname: %s" % outputfig

    plt.figure(figsize=(10,2))
    data = np.loadtxt(filename)
    plt.plot(data[:,0], data[:,1])
    plt.savefig(outputfig)
    plt.close()
