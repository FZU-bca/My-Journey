#The learning of Module
"""
[from + module name] import [module|class|function|*][as another name]   ----which [] means not required
import + module name
from + module name + import + xxx(import defined things)
from + module name + import + *(import all things)
import + module name + as + another name
from + module name + function names + as + another name
"""
import time   #how to watch how this Module includes : CTRL + click
time.sleep(5)
print("begins")
time.sleep(1)
print("ends")

from time import sleep
print("begins")
sleep(1)
print("ends")

from time import*
sleep(1)
print("begins")
sleep(1)
print("ends")

import time as t
print("begins")
t.sleep(1)
print("ends")

from time import sleep as sl
print("begins")
sl(1)
print("ends")