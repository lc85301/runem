project: runem
description:
In order to save the time to run em simulation on workstation
runem is designed to run em simulation offline using "at" command

goal:
1. call "at" command to run one em simulation
2. Monitor the running process, and send signal after process over
3. import mail module, send notification mail after em simulation over
4. create a batch of em files, continue next em after previous end

Language:
though using shell script is enough for "at" command
runem will write in python due to the mail module
