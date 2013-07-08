#!/usr/bin/env bash

PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin 
export PATH

find . -name *.cdslck -exec rm -fv {} \;
