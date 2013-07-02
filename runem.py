#!/usr/bin/env python

##############################################
# File: runem.py
# Description: the automatic run em
##############################################

import sys
import os.path
import subprocess
import shutil
#from optparse import OptionParser,make_option
#
#option_list = [
#	make_option("-f", "--file", action='store',dest='file', default=False)
#]
#parser = OptionParser(usage = 'Usage: autoEM [OPTION...] DATA...', option_list=option_list)
#
#options,args = parser.parse_args()
#print(args)

filename = sys.argv[1]

if not filename.endswith(".son"):
	sys.stderr.write("not a valid sonnet simulation file\n")
	sys.exit(0)

if not os.path.isfile(filename):
	sys.stderr.write("the simulation file doesn't exist\n")
	sys.exit(0)
#the file path of the simulation file
pathname = os.path.dirname(os.path.abspath(filename))
rawfilename = filename[:-4]
print(pathname)
print(rawfilename)

# if exist, remove the old running log directory
# otherwise em will stop simulation
setting="{0}/sondata/{1}".format(pathname, rawfilename)
if os.path.isdir(setting):
	shutil.rmtree(setting)

# now run the em simulation using em and "at" command
#command = ["echo","-v {0}".format(filename),"|", "at", "now +1 minutes"]
command = "echo 'em -v {0}' | at now +1 minutes".format(filename)
p  = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
p_stdout = p.stdout.read()
p_stderr = p.stderr.read()
