#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 14:01:39 2022

@author: robertgc
"""

from classroom import Student
from classroom import Teacher

print('------------------------------------------')

me = Student('Benedikt', 'Daurer', 'physics') 
me.printNameSubject() 

print('------------------------------------------')

filipe = Teacher('Filipe','Maia','Programming')
filipe.printNameCourse()