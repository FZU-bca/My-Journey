#The learning of python package
#There are many python module in a python package, also a project called "_init_.py" will be included
#Also, if there are no "_init_.py" in this package, it will not be a python package
def info_print():
    print("module1")

def my_module():
    print("module2")
#above are package and then we will see how to use them

import my_package.my_module
import my_package.info_print
my_package.my_module1.info_print()
my_package.my_module1.my_module()
#There are another way to use it
from my_package import my_module
from my_package import info_print
my_module.info_print()
my_module.my_module()
