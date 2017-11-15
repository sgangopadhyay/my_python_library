#!/usr/bin/python

# Programmed By : Suman Gangopadhyay
# Date : 10-May-2017

# Python program to verify the OS of your system
def OSCheck():
	if (platform.system()=="Linux"):
		return (platform.system(), platform.release(), platform.version(), platform.machine());
	elif(platform.system()=="Windows"):
		return (platform.system(), platform.release(), platform.version(), platform.machine());
	else:
		return ("Unknown OS");
print(OSCheck())


