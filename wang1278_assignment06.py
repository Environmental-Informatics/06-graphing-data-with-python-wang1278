#!/usr/bin/env python3
"""
Creator: Linji Wang (wang1278)
Date of Creation: 02/28/20
File Name: wang1278_assignment06.py
Discription:
    This script takes multiple file names as command line argument, reads data,
    plots data, and saves the plots into .pdf files for each file.
"""

# Import numply for reading data from files and matplotlib.pyplot for ploting
import numpy as np
import matplotlib.pyplot as plt
# Import argv from sys for parsing command line options
import sys
# Import os for removing file extensions
import os

# import data from files and use the first line as header
for i in range(len(sys.argv)):
    if i>0:
        data=np.genfromtxt(sys.argv[i],names=True,delimiter='\t')

    # Configure plot settings
        plt.figure(figsize=(15,15))
        plt.subplots_adjust(hspace=0.5)

    # Generate plots
        plt.subplot(311)
        plt.plot(data['Year'],data['Mean'], 'k',data['Year'],data['Max'], 'r',
                 data['Year'],data['Min'], 'b')
        plt.legend(["Mean","Max","Min"], loc='best',edgecolor='k')
        plt.xlabel("Year")
        plt.ylabel("Streamflow (cfs)")
        plt.subplot(312)
        plt.plot(data['Year'],data['Tqmean']*100, 'g^')
        plt.xlabel("Year")
        plt.ylabel("Tqmean (%)")
        plt.subplot(313)
        plt.bar(data['Year'],data['RBindex'])
        plt.xlabel("Year")
        plt.ylabel("R-B Index (ratio)")
        
        # Save plots in pdf
        savename=os.path.splitext(sys.argv[i])
        plt.savefig(savename[0]+'.pdf')
        plt.close()
print('Data Plotting Complete!')