#!/usr/bin/env python

__author__ = 'David Poslt'
__credits__ = ['David Poslt']
__copyrights__ = 'Copyright 2016'
__licence__= 'akorat s.r.o.'
__version__ = '1.0.1'
__email__ = 'david.poslt@gmail.com'
__status__ = 'production'


import os, datetime, sys
import shutil as su

target = r'path'
source = r'path'
freedisk = 5.0 #5GB free

def logWrite(string):
    file = open('backupAgins.log','a+')
    time = datetime.datetime.now()
    time = time.ctime()
    file.write(str(time)+' '+string+'\n')
    file.close()

    
def freeOnDrive(drive):
    free = float(su.disk_usage(drive)[2])
    free = free/1000000000
    
    if free < freedisk:
        logWrite('wrong disk space')
        sys.exit()


def isExists(folder):
    if os.path.exists(folder):
        return True
    else:
        logWrite('Folder '+folder+'donesn\'n exists')

def copy(source,target):
    freeOnDrive('/') #testing space of harddrive
    if isExists(source) == True and isExists(target) == True:
        try:
            su.copytree(source,target,symlinks=True, ignore=none)
            logWrite('Folder succsessfully copy')
        except:
            logWrite('error with copy')
    else:
        logWrite('path '+source+' or'+target+' doesn\'t exists ')
    
copy(source,target)

'''
if os.path.exists(target):
    freeOnDrive(target)

else:
    logWrite('path '+target+' does\'n exists')

'''


    
