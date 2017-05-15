#!/usr/bin/python
import subprocess
import sys
import os
from subprocess import Popen, PIPE

runlevl = Popen(['who -r'], shell=True, stdout=PIPE).stdout
val = runlevl.read()
retval = val.split()[1]
PI_HOME = '/opt/pisces/patterninsight/application/bin'


def status():
    subprocess.call(['/bin/su', '-', 'pisces', '-c', PI_HOME+'/pi status'])


def start():
    subprocess.call(['/bin/su', '-', 'pisces', '-c', PI_HOME+'/pi start'])


def stop():
    subprocess.call(['/bin/su', '-', 'pisces', '-c', PI_HOME+'/pi stop'])


try:
    if sys.argv[1] == 'start' or sys.argv[1] == 'START':
        start()
    elif sys.argv[1] == 'stop' or sys.argv[1] == 'STOP':
        stop()
    elif sys.argv[1] == 'status' or sys.argv[1] == 'STATUS':
        status()
    else:
        print "Usage: "+sys.argv[0]+" {start|stop|status}"
except IndexError:
    if retval >= '2' and retval <= '5':
        start()
    elif retval == '0' or retval == '1' or retval == '6':
        sys.exit()
    else:
        print "Usage: "+sys.argv[0]+" {start|stop|status}"
