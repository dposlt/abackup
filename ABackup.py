#!/usr/bin/env python

__author__ = 'David Poslt'
__credits__ = ['David Poslt']
__copyrights__ = 'Copyright 2016'
__licence__= 'akorat s.r.o.'
__version__ = '1.0.1'
__email__ = 'david.poslt@gmail.com'
__status__ = 'production'


import os, datetime
import shutil as su
target = r'C:/'
source = r'C:/Agnis/Database'

def logWrite(string):
    file = open('backupAgins.log','a+')
    time = datetime.datetime.now()
    file.write(str(time)+' '+string+'\n')
    file.close()

    
def freeOnDrive(drive):
    free = float(su.disk_usage(drive)[2])
    free = free/1000000000
    
    if free[2] > 5.0:
        logWrite('wrong disk space')
        end()



if os.path.exists(target):
    freeOnDrive(target)
    
else:
    logWrite('path '+target+' does\'n exists')



    
