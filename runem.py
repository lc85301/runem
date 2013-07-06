#!/usr/bin/env python

##################################################################################
#-*- coding: utf-8 -*-
# 
# Filename: runem.py
#
# Copyright (C) 2013 -  You-Tang Lee (YodaLee) <lc85301@gmail.com>
# All Rights reserved.
#
# This file is part of project: runem.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
##################################################################################

import sys
import os.path
import subprocess
import shutil
import smtplib
import getpass
from email.mime.text import MIMEText
import re

# parse option 
#from optparse import OptionParser,make_option
#
#option_list = [
#	make_option("-s", "--set", action='store',dest='file', default=False)
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

def sendmail(filename):
	"""get mail then sendmail"""
	sender = "lc85301@gmail.com"
	receiver = getmail()

	if receiver == "":
		return 0
	# open smtp session
	session = smtplib.SMTP('smtp.gmail.com', 587)
	session.ehlo
	session.starttls()
	session.ehlo
	session.login(account, password)

	# prepare the send message
	msg = MIMEText("Your EM simulation of {0} is over. Have a good day.".format())
	msg['Subject'] = "EM simulation is over"
	msg['From'] = sender
	msg['To'] = receiver

	# send the message
	session.sendmail(sender, [receiver], msg.as_string())
	session.quit()

def monitor_pid(pid):
	"""Monitor a pid, then send message"""
	sendmail(filename)

def getmail():
	"""allow user input mail and save into ~/.runem"""
	setting = ".runem"
	mail = input("Please input your email address: ")
	filepath = os.path.expanduser("~") + "/" + setting
	mailfile = None
	try:
		mailfile = open(filepath , mode="w")
		mailfile.write(mail)
	except IOError:
		pass
	finally:
		if mailfile is not None:
			mailfile.close()

def getpid():
	"""using ps to find the em simulation pid just called"""
	username = getusername()
	command = "ps -elf ｜ grep 'em -v' | grep {0} | grep [^grep] ｜ tr -s ' ' | cut -d ' ' -f 4 | sort -v".format(username)
	p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
	print(p.stdout)
	return pid

def getusername():
	"""get user name, to grep em process"""
	return getpass.getuser()

#filename = sys.argv[1]

#if not filename.endswith(".son"):
#	sys.stderr.write("not a valid sonnet simulation file\n")
#	sys.exit(0)
#
#if not os.path.isfile(filename):
#	sys.stderr.write("the simulation file doesn't exist\n")
#	sys.exit(0)
##the file path of the simulation file
#pathname = os.path.dirname(os.path.abspath(filename))
#rawfilename = filename[:-4]
#print(pathname)
#print(rawfilename)
#
## if exist, remove the old running log directory
## otherwise em will stop simulation
#setting="{0}/sondata/{1}".format(pathname, rawfilename)
#if os.path.isdir(setting):
#	shutil.rmtree(setting)
#
## now run the em simulation using em and "at" command
##command = ["echo","-v {0}".format(filename),"|", "at", "now +1 minutes"]
#command = "echo 'em -v {0}' | at now +1 minutes".format(filename)
#p  = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
#p_stdout = p.stdout.read()
#p_stderr = p.stderr.read()
