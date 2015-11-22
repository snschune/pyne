#!/usr/bin/python

import sys
import os
from pyne import ensdf

decay = ensdf.decays("234PA.decay")
for el in decay:
    print "Parent ID " , el[0], " branching  ratio ", el[5]	
