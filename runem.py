#!/usr/bin/env python

##############################################
# File: runem.py
# Description: the automatic run em
##############################################

import sys
import os.path
import subprocess
import shutil
import smtplib
from email.mime.text import MIMEText
import re
#from optparse import OptionParser,make_option
#
#option_list = [
#	make_option("-f", "--file", action='store',dest='file', default=False)
#]
#parser = OptionParser(usage = 'Usage: autoEM [OPTION...] DATA...', option_list=option_list)
#
#options,args = parser.parse_args()
#print(args)

def getmail():
	"""get user email if ~/.runem is exist"""
	setting = ".runem"
	filefullname = os.path.expanduser("~") + "/" + setting
	mailfile = None
	mail = ""
	try:
		mailfile = open(filefullname, mode="r")
		mail = mailfile.readline()
	except IOError:
		pass
	finally:
		if mailfile is not None:
			mailfile.close()
	return mail

def sendmail():
	"""get mail then sendmail"""
	sender = "lc85301@gmail.com"
	receiver = getmail()

	if receiver == "":
		return 0
	# open smtp session
	session  = smtplib.SMTP('smtp.gmail.com', 587)
	session.ehlo
	session.starttls()
	session.ehlo
	session.login(account, password)

	# prepare the send message
	msg = MIMEText("smtp module test")
	msg['Subject'] = "the test title"
	msg['From'] = sender
	msg['To'] = receiver

	# send the message
	session.sendmail(sender, [receiver], msg.as_string())
	session.quit()

sendmail()
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
