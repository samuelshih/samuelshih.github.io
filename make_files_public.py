#!/usr/bin/env python

import os
import sys

answer = raw_input('Are you sure you want to make the contents of this directory (%s) public?  Type \x1b[01;32myes\x1b[0m to proceed.\n' % os.getcwd())

if answer != 'yes':
    sys.exit(0)

def set_permissions(dir_name):
    entries = os.listdir(dir_name)
    os.chdir(dir_name)

    for entry in entries:
        if os.path.isdir(entry):
            os.system('chmod 755 %s' % entry)
            set_permissions(entry)
            os.chdir('..')
        else:
            os.system('chmod 644 %s' % entry)

set_permissions('.')
